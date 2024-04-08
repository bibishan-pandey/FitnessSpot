from django.urls import path

from . import views

app_name = 'auths'

urlpatterns = [
    path('register/', views.register, name='fitness-register'),
    path('login/', views.signin, name='fitness-login'),
    path('logout/', views.signout, name='fitness-logout'),
    path('my-profile/', views.my_profile, name='fitness-profile'),
    path('profile/<str:username>/', views.others_profile, name='fitness-others-profile'),
]
