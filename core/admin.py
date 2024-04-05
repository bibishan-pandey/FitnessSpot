from django.contrib import admin
from unfold.admin import ModelAdmin

from core.models import Post, WorkoutType, Workout


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
