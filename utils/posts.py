from django.db.models import Q

from core.models import Friend, Post, Comment, ReplyComment


def get_posts_with_comments(request, *args, **kwargs):
    # Get the IDs of the current users set in the user column of the friends table
    user_friends_ids = Friend.objects.filter(user=request.user).values_list('friend_id', flat=True)
    # Get the IDs of the current users set in the friend columns of the friends table
    user_users_ids = Friend.objects.filter(friend=request.user).values_list('friend_id', flat=True)
    friends = user_friends_ids | user_users_ids
    posts = (Post.objects
             .filter(
        Q(author=request.user) |  # Posts by the user
        Q(visibility="public") |  # Public posts
        (Q(visibility="friends") & Q(author__id__in=friends)),  # Posts visible to friends
        active=True,
        **kwargs
    ).order_by('-created_at'))
    # Fetch comments for each post separately
    post_comments = {}
    for post in posts:
        comments_qs = Comment.objects.filter(post=post)
        post_comments[post.id] = comments_qs

    # Fetch comment replies for each comment separately
    comment_replies = {}
    for comments_qs in post_comments.values():
        for comment in comments_qs:
            replies_qs = ReplyComment.objects.filter(comment=comment)
            comment_replies.setdefault(comment.id, []).extend(replies_qs)

    # Assign comments and comment replies to each post
    for post in posts:
        post.comments = post_comments.get(post.id, [])
        for comment in post.comments:
            comment.comment_replies = comment_replies.get(comment.id, [])
    return posts
