from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('log_workout/', views.log_workout, name='log_workout'),
    path('log_meal/', views.log_meal, name='log_meal'),
]
