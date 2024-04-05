from django.db import models

from core.models.base import BaseModel
from utils.choices import WORKOUT_CATEGORY


class WorkoutType(BaseModel):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255, choices=WORKOUT_CATEGORY, default='general_fitness')

    def __str__(self):
        return self.name
