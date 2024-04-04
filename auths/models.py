from django.contrib.auth.models import AbstractUser
from django.db import models


GENDER = (
    ("male", "Male"),
    ("female", "Female"),
    ("other", "Other"),
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
