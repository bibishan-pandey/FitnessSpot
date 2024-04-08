from core.models import FriendRequest


def context_processor(request):
    try:
        friend_request = FriendRequest.objects.filter(to_user=request.user)
    except:
        friend_request = None

    return {
        'friend_request': friend_request
    }
