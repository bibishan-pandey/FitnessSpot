# Notification keys
from core.models import Notification

NOTIFICATION_NEW_LIKE = 'new_like'
NOTIFICATION_NEW_COMMENT = 'new_comment'
NOTIFICATION_NEW_COMMENT_REPLY = 'new_comment_reply'
NOTIFICATION_NEW_FRIEND_REQUEST = 'new_friend_request'
NOTIFICATION_FRIEND_REQUEST_ACCEPTED = 'friend_request_accepted'

# Notification types
NOTIFICATION_TYPE = (
    ("new_like", "New like"),
    ("new_comment", "New comment"),
    ("new_comment_reply", "New comment reply"),
    ("new_friend_request", "New friend request"),
    ("friend_request_accepted", "Friend request accepted"),
)


def send_notification(from_user, to_user, post, comment, notification_type):
    """
    Send a notification to a user
    """
    notification = Notification.objects.create(
        from_user=from_user,
        to_user=to_user,
        post=post,
        comment=comment,
        notification_type=notification_type
    )
    return notification
