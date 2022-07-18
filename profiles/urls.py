from django.urls import path
from . import views

app_name = 'profiles'

urlpatterns = [
    path('myprofile/', views.myprofile, name='myprofile'),
    path('createprofile/', views.createprofile, name = 'createprofile')
]