from django.urls import path
from . import views
from django.contrib.auth import login

app_name = 'users'

urlpatterns = [
    path('register/', views.registration, name='register'),
    # path('profile/', views.profile, name='profile')
]