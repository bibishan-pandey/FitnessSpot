from django.db import models
from shortuuid.django_fields import ShortUUIDField

from auths.models import User
from core.models.base import BaseModel

FRIEND_REQUEST_STATUS = (
    ('pending', 'Pending'),
    ('accepted', 'Accepted'),
    ('rejected', 'Rejected'),
)


class FriendRequest(BaseModel):
    fid = ShortUUIDField(length=8, max_length=26, alphabet='abcdefghijklmnopqrstuvqxyz', unique=True)
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='from_user')
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='to_user')
    status = models.CharField(max_length=15, choices=FRIEND_REQUEST_STATUS, default='pending')

    def __str__(self):
        if self.from_user and self.to_user:
            return self.from_user.username + " to " + self.to_user.username
        return self.fid
