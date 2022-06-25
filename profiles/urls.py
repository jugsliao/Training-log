from django.urls import path
from . import views

app_name = 'profiles'

urlpatterns = [
    path('', views.ProfilesList.as_view(), name='profiles'),
    path('<int:profile_id>', views.profile, name='profile'),
    path('myprofile/', views.myprofile, name='myprofile'),
    path('createprofile/', views.createprofile, name = 'createprofile')
]