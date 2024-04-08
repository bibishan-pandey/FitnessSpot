from django.db import models
from shortuuid.django_fields import ShortUUIDField

from auths.models import User
from core.models.base import BaseModel
from core.models.workout_type import WorkoutType


class Workout(BaseModel):
    uid = ShortUUIDField(length=8, max_length=26, alphabet='abcdefghijklmnopqrstuvqxyz', unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    start_time = models.TimeField(null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    type = models.ForeignKey(WorkoutType, on_delete=models.CASCADE)
    duration = models.DurationField(null=True, blank=True)
    calories_burned = models.FloatField(null=True, blank=True)
    distance = models.FloatField(null=True, blank=True)
    pace = models.FloatField(null=True, blank=True)
    elevation = models.FloatField(null=True, blank=True)
    steps = models.PositiveIntegerField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    heart_rate = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return self.name
