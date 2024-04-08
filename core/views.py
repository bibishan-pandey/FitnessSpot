from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.utils.timesince import timesince
from django.views.decorators.csrf import csrf_exempt

from auths.models import User
from core.models import Post, Workout, Comment, ReplyComment, FriendRequest
from utils.posts import get_posts_with_comments


@login_required
def index(request):
    posts = get_posts_with_comments(request)

    workouts = Workout.objects.filter(author=request.user)

    # Add others count to each post to show the number of other people who liked the post
    # And for the first person who liked the post, we don't want to show the count instead
    # we show the name of that person
    # for post in posts:
    #     post.others_count = post.likes.all().count() - 1 if post.likes.all().count() > 1 else 0

    context = {
        'posts': posts,
        'workouts': workouts
    }

    return render(request, 'core/index.html', context)


@login_required
def post_detail(request, slug):
    post = get_posts_with_comments(request, slug=slug)
    if not post:
        return JsonResponse({'error': 'Post not found'}, status=404)

    context = {
        "post": post[0]
    }
    return render(request, "core/post-detail.html", context)


@csrf_exempt
@login_required
def create_post(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'Method not allowed'}, status=405)

    content = request.POST.get('post-caption')
    image = request.FILES.get('post-thumbnail')
    video = request.FILES.get('video')
    workout_id = request.POST.get('workout')

    # check if workout_id is valid
    if workout_id:
        try:
            workout_id = int(workout_id)
        except ValueError:
            workout_id = None

    visibility = request.POST.get('visibility')
    active = request.POST.get('active')

    if content or image or video or workout_id:
        post_data = {
            'author': request.user,
            'visibility': visibility,
        }

        if content:
            post_data['content'] = content
        if image:
            post_data['image'] = image
        if video:
            post_data['video'] = video
        if workout_id:
            workout = Workout.objects.get(id=workout_id)
            post_data['workout'] = workout
        if active:
            post_data['active'] = active

        post = Post.objects.create(**post_data)
        post.save()

        # Serialize the post object
        serialized_post = serializers.serialize('json', [post])
        return JsonResponse({'data': serialized_post})

    return JsonResponse({'error': 'Unprocessable Entity'}, status=422)


@csrf_exempt
@login_required
def like_post(request):
    _id = request.GET.get('id')
    post = get_object_or_404(Post, id=_id)
    user = request.user

    if user in post.likes.all():
        post.likes.remove(user)
        is_liked = False
    else:
        post.likes.add(user)
        is_liked = True

    likes_count = post.likes.count()

    data = {
        "is_liked": is_liked,
        'likes': likes_count
    }
    return JsonResponse({"data": data})


@csrf_exempt
@login_required
def delete_post(request):
    _id = request.GET.get('id')
    post = get_object_or_404(Post, id=_id)
    if post.author.id == request.user.id:
        post.delete()
        return JsonResponse({"data": "Post deleted successfully"})
    return JsonResponse({"error": "Unauthorized"}, status=401)


@csrf_exempt
@login_required
def comment_post(request):
    _id = request.GET.get('id')
    comment = request.GET.get('comment')
    post = Post.objects.get(id=_id)
    comment_count = Comment.objects.filter(post=post).count()

    new_comment = Comment.objects.create(
        post=post,
        comment=comment,
        user=request.user
    )

    data = {
        'comment': new_comment.comment,
        "profile_image": new_comment.user.profile.avatar.url,
        "date": timesince(new_comment.updated_at),
        "comment_id": new_comment.id,
        "post_id": new_comment.post.id,
        "comment_count": comment_count + int(1)
    }
    return JsonResponse({"data": data})


@csrf_exempt
@login_required
def delete_comment(request):
    _id = request.GET.get('id')
    comment = get_object_or_404(Comment, id=_id)
    if comment.user.id == request.user.id:
        comment.delete()
        return JsonResponse({"data": "Comment deleted successfully"})
    return JsonResponse({"error": "Unauthorized"}, status=401)


@csrf_exempt
@login_required
def reply_comment(request):
    _id = request.GET.get('id')
    reply = request.GET.get('reply')
    comment = get_object_or_404(Comment, id=_id)

    new_reply = ReplyComment.objects.create(
        comment=comment,
        reply=reply,
        user=request.user
    )

    data = {
        'reply': new_reply.reply,
        "profile_image": new_reply.user.profile.avatar.url,
        "date": timesince(new_reply.updated_at),
        "reply_id": new_reply.id,
        "comment_id": new_reply.comment.id
    }
    return JsonResponse({"data": data})


@csrf_exempt
@login_required
def add_friend(request):
    from_user = request.user
    receiver_id = request.GET.get('id')

    if from_user.id == int(receiver_id):
        return JsonResponse({'error': 'You cannot send a friend request to yourself.'})

    to_user = User.objects.get(id=receiver_id)

    try:
        friend_request = FriendRequest.objects.get(from_user=from_user, to_user=to_user)
        if friend_request:
            friend_request.delete()
        return JsonResponse({'is_friend_request_sent': False})
    except FriendRequest.DoesNotExist:
        friend_request = FriendRequest(from_user=from_user, to_user=to_user)
        friend_request.save()
        return JsonResponse({'is_friend_request_sent': True})
