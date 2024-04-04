from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.db import models
from django.http import HttpRequest
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _
from unfold.admin import ModelAdmin
from unfold.contrib.forms.widgets import WysiwygWidget
from unfold.decorators import action
from unfold.forms import UserChangeForm, UserCreationForm, AdminPasswordChangeForm

from auths.models import User, Profile


@admin.register(User)
class UserAdmin(BaseUserAdmin, ModelAdmin):
    # Preprocess content of readonly fields before render
    readonly_preprocess_fields = {
        "model_field_name": "html.unescape",
        "other_field_name": lambda content: content.strip(),
    }

    # Display submit button in filters
    list_filter_submit = True

    # Custom actions
    actions_list = []  # Displayed above the results list
    actions_row = []  # Displayed in a table row in results list
    actions_detail = []  # Displayed at the top of for in object detail
    actions_submit_line = ['submit_line_action_activate']  # Displayed near save in object detail

    ordering = ('username', 'email', 'first_name', 'last_name', 'is_active', 'is_staff', 'is_superuser', 'date_joined')

    formfield_overrides = {
        models.TextField: {
            "widget": WysiwygWidget,
        }
    }

    form = UserChangeForm
    add_form = UserCreationForm
    change_password_form = AdminPasswordChangeForm

    @action(description=_("Save & Activate"))
    def submit_line_action_activate(self, request: HttpRequest, obj: User):
        """
        If instance is modified in any way, it also needs to be saved,
        since this handler is invoked after instance is saved.
        :param request:
        :param obj: Model instance that was manipulated, with changes already saved to database
        :return: None, this handler should not return anything
        """
        obj.is_active = True
        obj.save()


@admin.register(Profile)
class ProfileAdmin(ModelAdmin):
    # Preprocess content of readonly fields before render
    readonly_preprocess_fields = {
        "model_field_name": "html.unescape",
        "other_field_name": lambda content: content.strip(),
    }

    # Display submit button in filters
    list_filter_submit = True

    ordering = ('user', 'verified', 'created_at', 'updated_at')
    list_display = ('user', 'phone', 'gender', 'verified', 'created_at', 'updated_at', 'display_avatar')
    sortable_by = ('user', 'verified', 'created_at', 'updated_at')

    def display_avatar(self, obj):
        return format_html('<img src="{}" width="50px" height="50px" />', obj.avatar.url)

    display_avatar.short_description = 'Avatar'
    display_avatar.allow_tags = True
