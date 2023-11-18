from django.urls import path
from . import views

urlpatterns = [
    path('', views.members, name='home'),
    path('topics/', views.topics, name='topics'),
    path('rewards/', views.rewards, name='rewards'),
]