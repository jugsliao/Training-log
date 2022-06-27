from django.urls import path
from . import views

app_name = "traininglog"

urlpatterns = [
    path('', views.home, name='home'),
    path('newlog/', views.newlog, name='newlog'),
    path('logs/', views.LogsView.as_view(), name='logs'),
    path('logs/<int:log_id>', views.log, name='log')
]