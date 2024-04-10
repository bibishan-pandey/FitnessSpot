from core.models import FriendRequest, Notification, WorkoutType, Workout, Friend


def context_processor(request):
    try:
        friend_request = FriendRequest.objects.filter(to_user=request.user).order_by('-created_at')
    except:
        friend_request = None

    try:
        notification = Notification.objects.filter(to_user=request.user).order_by('-created_at')
    except:
        notification = None

    try:
        workout_types = WorkoutType.objects.all()
    except:
        workout_types = None

    try:
        workouts = Workout.objects.filter(author=request.user)
    except:
        workouts = None

    try:
        my_friends_from_user = Friend.objects.filter(user=request.user)
        my_friends_to_user = Friend.objects.filter(friend=request.user)
        my_friends = my_friends_from_user | my_friends_to_user
    except:
        my_friends = None

    return {
        'friend_request': friend_request,
        'notification': notification,
        'workout_types': workout_types,
        'workouts': workouts,
        'my_friends': my_friends if 'my_friends' in locals() else None  # Ensure friends is defined even if there's an error
    }
