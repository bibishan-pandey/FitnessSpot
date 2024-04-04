from django.contrib.auth.forms import (UserCreationForm as AuthUserCreationForm)

from .models import User


class UserCreationForm(AuthUserCreationForm):
    class Meta(AuthUserCreationForm.Meta):
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'phone', 'gender', 'password1', 'password2')
