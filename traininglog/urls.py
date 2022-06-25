from django.urls import path
from . import views

app_name = "traininglog"

urlpatterns = [
    path('', views.home, name='home'),
    path('newlog/', views.newlog, name='newlog'),
    # path('log/', views.LogView.as_view(), name='log'),
]