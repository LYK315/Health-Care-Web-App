from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('findadoctor/', views.findadoctor),
    path('login/', views.login),
    path('register/', views.register),
    path('specialities/', views.specialities),
]


# Create your views here.
