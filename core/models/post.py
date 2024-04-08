import shortuuid
from django.db import models
from django.utils.safestring import mark_safe
from django.utils.text import slugify
from shortuuid.django_fields import ShortUUIDField

from auths.models import User
from core.models.base import BaseModel
from core.models.workout import Workout
from utils.choices import VISIBILITY
from utils.media_upload import upload_post_image_location, upload_post_video_location


class Post(BaseModel):
    uid = ShortUUIDField(length=8, max_length=26, alphabet='abcdefghijklmnopqrstuvqxyz', unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to=upload_post_image_location, blank=True, null=True)
    video = models.FileField(upload_to=upload_post_video_location, blank=True, null=True)
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE, null=True, blank=True)
    slug = models.SlugField(max_length=255, unique=True, null=True, blank=True)
    visibility = models.CharField(max_length=15, choices=VISIBILITY, default='public')
    likes = models.ManyToManyField(User, related_name='post_likes', blank=True)
    active = models.BooleanField(null=True, blank=True, default=True)
    views = models.PositiveIntegerField(default=0)

    def save(self, *args, **kwargs):
        if self.slug is None or self.slug == "":
            uuid_key = shortuuid.uuid()
            self.slug = str(uuid_key.lower()) + "-" + slugify(self.content[:10] if self.content else "")
        super(Post, self).save(*args, **kwargs)

    def thumbnail(self):
        return mark_safe(
            '<img src="/media/%s" width="50" height="50" object-fit:"cover" style="border-radius: 5px;" />' %
            self.image
        )

    def __str__(self):
        if self.content:
            return self.content
        return self.author.username
