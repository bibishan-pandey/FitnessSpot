from django.contrib import admin
from unfold.admin import ModelAdmin

from core.models import (
    Post,
    Community,
    CommunityPost,
    WorkoutType,
    Workout,
    FriendRequest,
    Friend,
    Comment,
    ReplyComment,
    Notification
)


@admin.register(WorkoutType)
class WorkoutTypeAdmin(admin.ModelAdmin):
    # Display submit button in filters
    list_filter_submit = True

    ordering = ('name', 'category', 'created_at', 'updated_at')
    list_display = ('name', 'category', 'created_at', 'updated_at')
    sortable_by = ('name', 'category', 'created_at', 'updated_at')


@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    # Display submit button in filters
    list_filter_submit = True

    ordering = ('uid', 'author', 'name', 'type', 'created_at', 'updated_at')
    list_display = ('uid', 'author', 'name', 'type', 'created_at', 'updated_at')
    sortable_by = ('uid', 'author', 'name', 'type', 'created_at', 'updated_at')


@admin.register(Post)
class PostAdmin(ModelAdmin):
    # Preprocess content of readonly fields before render
    readonly_preprocess_fields = {
        "model_field_name": "html.unescape",
        "other_field_name": lambda content: content.strip(),
    }

    # Display submit button in filters
    list_filter_submit = True

    ordering = ('uid', 'author', 'content', 'slug', 'visibility', 'active', 'views', 'created_at', 'updated_at')
    list_display = ('uid', 'author', 'content', 'slug', 'visibility', 'active', 'views', 'created_at', 'updated_at')
    sortable_by = ('uid', 'author', 'content', 'slug', 'visibility', 'active', 'views', 'created_at', 'updated_at')


@admin.register(FriendRequest)
class FriendRequestAdmin(admin.ModelAdmin):
    # Display submit button in filters
    list_filter_submit = True

    ordering = ('uid', 'from_user', 'to_user', 'status', 'created_at', 'updated_at')
    list_display = ('uid', 'from_user', 'to_user', 'status', 'created_at', 'updated_at')
    sortable_by = ('uid', 'from_user', 'to_user', 'status', 'created_at', 'updated_at')


@admin.register(Friend)
class FriendAdmin(admin.ModelAdmin):
    # Display submit button in filters
    list_filter_submit = True

    ordering = ('uid', 'user', 'friend', 'created_at', 'updated_at')
    list_display = ('uid', 'user', 'friend', 'created_at', 'updated_at')
    sortable_by = ('uid', 'user', 'friend', 'created_at', 'updated_at')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    # Display submit button in filters
    list_filter_submit = True

    ordering = ('uid', 'user', 'post', 'comment', 'active', 'created_at', 'updated_at')
    list_display = ('uid', 'user', 'post', 'comment', 'active', 'created_at', 'updated_at')
    sortable_by = ('uid', 'user', 'post', 'comment', 'active', 'created_at', 'updated_at')


@admin.register(ReplyComment)
class ReplyCommentAdmin(admin.ModelAdmin):
    # Display submit button in filters
    list_filter_submit = True

    ordering = ('uid', 'user', 'comment', 'reply', 'active', 'created_at', 'updated_at')
    list_display = ('uid', 'user', 'comment', 'reply', 'active', 'created_at', 'updated_at')
    sortable_by = ('uid', 'user', 'comment', 'reply', 'active', 'created_at', 'updated_at')


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    # Display submit button in filters
    list_filter_submit = True

    ordering = ('uid', 'from_user', 'to_user', 'post', 'comment',
                'notification_type', 'read', 'created_at', 'updated_at')
    list_display = ('uid', 'from_user', 'to_user', 'post', 'comment',
                    'notification_type', 'read', 'created_at', 'updated_at')
    sortable_by = ('uid', 'from_user', 'to_user', 'post', 'comment',
                   'notification_type', 'read', 'created_at', 'updated_at')


@admin.register(Community)
class CommunityAdmin(admin.ModelAdmin):
    # Display submit button in filters
    list_filter_submit = True

    ordering = ('uid', 'owner', 'name', 'slug', 'visibility', 'active', 'views', 'created_at', 'updated_at')
    list_display = ('uid', 'owner', 'name', 'slug', 'visibility', 'active', 'views', 'created_at', 'updated_at')
    sortable_by = ('uid', 'owner', 'name', 'slug', 'visibility', 'active', 'views', 'created_at', 'updated_at')


@admin.register(CommunityPost)
class CommunityPostAdmin(ModelAdmin):
    # Preprocess content of readonly fields before render
    readonly_preprocess_fields = {
        "model_field_name": "html.unescape",
        "other_field_name": lambda content: content.strip(),
    }

    # Display submit button in filters
    list_filter_submit = True

    ordering = ('uid', 'community', 'content', 'slug', 'visibility', 'active', 'views', 'created_at', 'updated_at')
    list_display = ('uid', 'community', 'content', 'slug', 'visibility', 'active', 'views', 'created_at', 'updated_at')
    sortable_by = ('uid', 'community', 'content', 'slug', 'visibility', 'active', 'views', 'created_at', 'updated_at')
