from django.urls import path

from . import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='fitness-feed'),

    # Ajax endpoints
    path('create-post/', views.create_post, name='create-post'),
    path('like-post/', views.like_post, name='like-post'),
]
