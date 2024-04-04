import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models
from shortuuid.django_fields import ShortUUIDField

GENDER = (
    ("male", "Male"),
    ("female", "Female"),
    ("other", "Other"),
)

RELATIONSHIP = (
    ("single", "Single"),
    ("married", "Married"),
    ("divorced", "Divorced"),
    ("widowed", "Widowed"),
)


def upload_location(instance, filename, upload_type="avatar"):
    # check if the file is an image and has an extension
    if not filename.endswith('.jpg') and not filename.endswith('.png') and not filename.endswith('.jpeg'):
        raise Exception("File is not supported. Please upload an image (jpg, png, jpeg) file.")

    extension = filename.split('.')[-1]
    filename = f"{instance.user.profile.pid}_{uuid.uuid4()}.{extension}"
    file_path = f'profiles/{instance.user.username}/{upload_type}/{filename}'
    return file_path


def upload_avatar_location(instance, filename):
    return upload_location(instance, filename, "avatar")


def upload_cover_location(instance, filename):
    return upload_location(instance, filename, "cover")


class User(AbstractUser):
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=10, blank=True, null=True)
    gender = models.CharField(max_length=6, choices=GENDER, blank=True, null=True)
    otp = models.CharField(max_length=6, blank=True, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.username


class Profile(models.Model):
    pid = ShortUUIDField(length=7, max_length=26, alphabet='abcdefghijklmnopqrstuvqxyz', unique=True, primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cover = models.ImageField(upload_to=upload_cover_location, default="avatar.jpg", blank=True, null=True)
    avatar = models.ImageField(upload_to=upload_avatar_location, default="cover.jpg", blank=True, null=True)
    phone = models.CharField(max_length=10, blank=True, null=True)
    gender = models.CharField(max_length=6, choices=GENDER, blank=True, null=True)
    height = models.FloatField(blank=True, null=True)
    weight = models.FloatField(blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    about_me = models.CharField(max_length=200, blank=True, null=True)
    bio = models.TextField(blank=True)
    relationship_status = models.CharField(max_length=10, choices=RELATIONSHIP, blank=True, null=True)

    country = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    postal_code = models.CharField(max_length=6, blank=True, null=True)

    working_at = models.CharField(max_length=100, blank=True, null=True)
    working_as = models.CharField(max_length=100, blank=True, null=True)
    working_since = models.DateField(blank=True, null=True)

    social_facebook = models.URLField(max_length=200, blank=True, null=True)
    social_instagram = models.URLField(max_length=200, blank=True, null=True)
    social_twitter = models.URLField(max_length=200, blank=True, null=True)
    social_youtube = models.URLField(max_length=200, blank=True, null=True)
    social_website = models.URLField(max_length=200, blank=True, null=True)

    verified = models.BooleanField(default=False)
    followers = models.ManyToManyField(User, related_name="followers", blank=True)
    following = models.ManyToManyField(User, related_name="following", blank=True)
    friends = models.ManyToManyField(User, related_name="friends", blank=True)
    blocked = models.ManyToManyField(User, related_name="blocked", blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username
