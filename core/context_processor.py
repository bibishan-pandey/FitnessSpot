from core.models import FriendRequest, Notification, WorkoutType


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

    return {
        'friend_request': friend_request,
        'notification': notification,
        'workout_types': workout_types
    }
