from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.ApiOverview, name='api-overview'),
    path('task-read/<str:pk>/', views.TaskRead, name='task-read'),
    path('task-create/', views.TaskCreate, name='task-create'),
    path('task-update/<str:pk>/', views.TaskUpdate, name='task-update')
]