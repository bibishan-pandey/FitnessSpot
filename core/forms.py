from django import forms

from .models import WorkoutType


class WorkoutTypeForm(forms.ModelForm):
    class Meta:
        model = WorkoutType
        fields = ('name', 'category')
