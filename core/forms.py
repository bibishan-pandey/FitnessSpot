from django import forms

from utils.choices import WORKOUT_CATEGORY
from .models import WorkoutType, Workout


class WorkoutTypeForm(forms.ModelForm):
    class Meta:
        model = WorkoutType
        fields = ('name', 'category')


class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = ['name', 'start_time', 'start_date', 'type', 'duration', 'calories_burned',
                  'distance', 'pace', 'elevation', 'steps', 'notes', 'heart_rate']
        widgets = {
            'type': forms.Select(choices=WORKOUT_CATEGORY),
            'start_time': forms.TimeInput(attrs={'type': 'time'}),
            'start_date': forms.DateInput(attrs={'type': 'date'}),
        }
