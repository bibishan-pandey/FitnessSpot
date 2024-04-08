from django.db.models import Q

from core.models import Friend, Post, Comment


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
        post_comments[post.id] = Comment.objects.filter(post=post)
    # Annotate posts with prefetched comments
    for post in posts:
        post.comments = post_comments.get(post.id, [])
    return posts
