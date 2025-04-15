from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('share_confession', views.share_confessions, name='share_confession'),
    path('confession/', views.view_random_confession, name='view_random_confession'),
]