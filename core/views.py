from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from core.models import Post, Workout


@login_required
def index(request):
    # TODO: Fix for friends posts
    posts = (Post.objects
             .filter(Q(visibility="public") | Q(author__friends__user=request.user), active=True)
             .order_by('-created_at'))

    workouts = Workout.objects.filter(author=request.user)

    context = {
        'posts': posts,
        'workouts': workouts
    }

    return render(request, 'core/index.html', context)


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
