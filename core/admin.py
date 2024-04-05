from django.contrib import admin
from unfold.admin import ModelAdmin

from core.models import Post, WorkoutType, Workout, FriendRequest, Friend, Comment, ReplyComment, Notification


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

    ordering = ('pid', 'author', 'name', 'type', 'created_at', 'updated_at')
    list_display = ('pid', 'author', 'name', 'type', 'created_at', 'updated_at')
    sortable_by = ('pid', 'author', 'name', 'type', 'created_at', 'updated_at')


@admin.register(Post)
class PostAdmin(ModelAdmin):
    # Preprocess content of readonly fields before render
    readonly_preprocess_fields = {
        "model_field_name": "html.unescape",
        "other_field_name": lambda content: content.strip(),
    }

    # Display submit button in filters
    list_filter_submit = True

    ordering = ('pid', 'author', 'content', 'slug', 'visibility', 'active', 'views', 'created_at', 'updated_at')
    list_display = ('pid', 'author', 'content', 'slug', 'visibility', 'active', 'views', 'created_at', 'updated_at')
    sortable_by = ('pid', 'author', 'content', 'slug', 'visibility', 'active', 'views', 'created_at', 'updated_at')


@admin.register(FriendRequest)
class FriendRequestAdmin(admin.ModelAdmin):
    # Display submit button in filters
    list_filter_submit = True

    ordering = ('fid', 'from_user', 'to_user', 'status', 'created_at', 'updated_at')
    list_display = ('fid', 'from_user', 'to_user', 'status', 'created_at', 'updated_at')
    sortable_by = ('fid', 'from_user', 'to_user', 'status', 'created_at', 'updated_at')


@admin.register(Friend)
class FriendAdmin(admin.ModelAdmin):
    # Display submit button in filters
    list_filter_submit = True

    ordering = ('fid', 'user', 'friend', 'created_at', 'updated_at')
    list_display = ('fid', 'user', 'friend', 'created_at', 'updated_at')
    sortable_by = ('fid', 'user', 'friend', 'created_at', 'updated_at')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    # Display submit button in filters
    list_filter_submit = True

    ordering = ('cid', 'user', 'post', 'comment', 'active', 'created_at', 'updated_at')
    list_display = ('cid', 'user', 'post', 'comment', 'active', 'created_at', 'updated_at')
    sortable_by = ('cid', 'user', 'post', 'comment', 'active', 'created_at', 'updated_at')


@admin.register(ReplyComment)
class ReplyCommentAdmin(admin.ModelAdmin):
    # Display submit button in filters
    list_filter_submit = True

    ordering = ('rcid', 'user', 'comment', 'reply', 'active', 'created_at', 'updated_at')
    list_display = ('rcid', 'user', 'comment', 'reply', 'active', 'created_at', 'updated_at')
    sortable_by = ('rcid', 'user', 'comment', 'reply', 'active', 'created_at', 'updated_at')


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    # Display submit button in filters
    list_filter_submit = True

    ordering = ('nid', 'from_user', 'to_user', 'post', 'comment',
                'notification_type', 'read', 'created_at', 'updated_at')
    list_display = ('nid', 'from_user', 'to_user', 'post', 'comment',
                    'notification_type', 'read', 'created_at', 'updated_at')
    sortable_by = ('nid', 'from_user', 'to_user', 'post', 'comment',
                   'notification_type', 'read', 'created_at', 'updated_at')
