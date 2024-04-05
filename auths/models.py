import shortuuid
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.utils.text import slugify
from shortuuid.django_fields import ShortUUIDField

from utils.media_upload import upload_cover_location, upload_avatar_location

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

    slug = models.SlugField(unique=True, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if self.slug is None or self.slug == "":
            uuid_key = shortuuid.uuid()
            slug_value = self.user.username if self.user.first_name is None or self.user.first_name == "" else self.user.first_name
            self.slug = slugify(slug_value) + "-" + str(uuid_key[:3].lower())
        super(Profile, self).save(*args, **kwargs)

    def __str__(self):
        return self.user.username


def create_user_profile(sender, instance, created, **kwargs):
    """
    Create a user profile when a new user is created.

    Using Django signals, we can create a user profile when a new user is created.
    """
    if created:
        Profile.objects.create(user=instance)


def save_user_profile(sender, instance, **kwargs):
    """
    Save the user profile when a user is saved.

    Using Django signals, we can save the user profile when a user is saved.
    """
    instance.profile.save()


post_save.connect(create_user_profile, sender=User)
post_save.connect(save_user_profile, sender=User)
