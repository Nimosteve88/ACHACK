from django.urls import path
from . import views

urlpatterns = [
    path('', views.members, name='home'),
    path('quiz1/', views.quiz1, name='quiz1'),
    path('rewards_eas/', views.rewards_eas, name='rewards_eas'),
    path('rewards_other/', views.rewards_other, name='rewards_other'),
    path('quiz2/', views.quiz2, name='quiz2'),
    path('facts/', views.facts, name='facts'),
    path('belongingToACommunity/', views.belongingToACommunity, name='belongingToACommunity'),
    path('energyAndSustainability/', views.energyAndSustainability, name='energyAndSustainability'),
    path('financialLiteracy/', views.financialLiteracy, name='financialLiteracy'),
    path('healthyRelationships/', views.healthyRelationships, name='healthyRelationships'),
    path('keepingFit/', views.keepingFit, name='keepingFit'),
    path('mentalHealthAndWellBeing/', views.mentalHealthAndWellBeing, name='mentalHealthAndWellBeing'),
    path('login/', views.login, name='login'),
]