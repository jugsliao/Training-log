from django.urls import path
from . import views

app_name = "traininglog"

urlpatterns = [
    path('register/', views.registration, name='register'),

    path('', views.home, name='home'),
    path('newlog/', views.newlogView.as_view(), name='newlog'),
    path('editlog/<int:log_id>', views.editlog, name='editlog'),
    path('deletelog/<int:log_id>', views.deletelog, name='deletelog'),
    path('logs/', views.LogsView.as_view(), name='logs'),
    path('logs/<int:log_id>', views.log, name='log'),

    path('newgoal/', views.newGoalView.as_view(), name='newgoal'),
    path('goals/', views.GoalsView.as_view(), name='goals'),
    path('goal', views.goal, name='goal'),
]