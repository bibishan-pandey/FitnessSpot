from django import forms
from django.contrib.auth.forms import (UserCreationForm as AuthUserCreationForm)

from .models import User, Profile


class UserCreationForm(AuthUserCreationForm):
    class Meta(AuthUserCreationForm.Meta):
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'phone', 'gender', 'password1', 'password2')


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('cover', 'avatar', 'phone', 'gender', 'height', 'weight', 'dob', 'about_me', 'bio',
                  'relationship_status', 'country', 'city', 'address', 'postal_code', 'working_at',
                  'working_as', 'working_since', 'social_facebook', 'social_instagram', 'social_twitter',
                  'social_youtube', 'social_website')
