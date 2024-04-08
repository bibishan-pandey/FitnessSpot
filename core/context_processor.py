from core.models import FriendRequest, Notification


def context_processor(request):
    try:
        friend_request = FriendRequest.objects.filter(to_user=request.user).order_by('-created_at')
    except:
        friend_request = None

    try:
        notification = Notification.objects.filter(to_user=request.user).order_by('-created_at')
        print(notification)
    except:
        notification = None

    return {
        'friend_request': friend_request,
        'notification': notification
    }
