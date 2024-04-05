from django.db import models
from shortuuid.django_fields import ShortUUIDField

from auths.models import User
from core.models.base import BaseModel
from .post import Post


class Comment(BaseModel):
    cid = ShortUUIDField(length=8, max_length=26, alphabet='abcdefghijklmnopqrstuvqxyz', unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.TextField(max_length=1000)
    likes = models.ManyToManyField(User, related_name='comment_likes', blank=True)
    active = models.BooleanField(default=True, null=True, blank=True)

    def __str__(self):
        return self.comment


class ReplyComment(BaseModel):
    rcid = ShortUUIDField(length=8, max_length=26, alphabet='abcdefghijklmnopqrstuvqxyz', unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    reply = models.TextField(max_length=1000)
    active = models.BooleanField(default=True, null=True, blank=True)

    def __str__(self):
        return self.reply
