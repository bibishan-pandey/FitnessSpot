from django.db import models
from shortuuid.django_fields import ShortUUIDField

from auths.models import User
from core.models.base import BaseModel
from .comment import Comment
from .post import Post

NOTIFICATION_TYPE = (
    ("new_like", "New like"),
    ("new_comment", "New comment"),
    ("new_comment_reply", "New comment reply"),
    ("new_friend_request", "New friend request"),
    ("friend_request_accepted", "Friend request accepted"),
)


class Notification(BaseModel):
    uid = ShortUUIDField(length=8, max_length=26, alphabet='abcdefghijklmnopqrstuvqxyz', unique=True)
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notification_from_user')
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notification_to_user')
    post = models.ForeignKey(Post, on_delete=models.SET_NULL, null=True, blank=True)
    comment = models.ForeignKey(Comment, on_delete=models.SET_NULL, null=True, blank=True)
    notification_type = models.CharField(max_length=30, choices=NOTIFICATION_TYPE)
    read = models.BooleanField(default=False, null=True, blank=True)

    # class Meta:
    #     unique_together = ['from_user', 'to_user']

    def __str__(self):
        if self.from_user and self.to_user:
            return self.from_user.username + " to " + self.to_user.username
        return self.uid
