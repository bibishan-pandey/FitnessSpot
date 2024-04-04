from django.urls import path

from . import views

app_name = 'auths'

urlpatterns = [
    path('register/', views.register, name='fitness-register'),
    path('login/', views.signin, name='fitness-login'),
]
