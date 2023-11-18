from django.urls import path
from . import views

urlpatterns = [
    path('', views.members, name='members'),
    path('quiz1/', views.quiz1, name='quiz1'),
    path('rewards/', views.rewards, name='rewards'),
    path('quiz2/', views.quiz2, name='quiz2'),
    path('facts/', views.facts, name='facts'),
]