from django.urls import path
from . import views

urlpatterns = [
    path('', views.members, name='members'),
    path('quiz1/', views.topics, name='quiz1'),
    path('rewards/', views.rewards, name='rewards'),
    path('quiz2/', views.topics, name='quiz2'),
    path('facts/', views.topics, name='facts'),
]