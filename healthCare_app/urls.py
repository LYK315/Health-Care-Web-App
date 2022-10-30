from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('findadoctor/', views.findadoctor, name="findadoctor"),
    path('register/', views.register, name="register"),
    path('postRegister/', views.postRegister, name="postRegister"),
     path('postLogin/', views.postLogin, name="postLogin"),
    path('specialities/', views.specialities, name="specialities"),
    path('healthcareblog/', views.healthcareblog, name="healthcareblog"),
    path('ourservices/', views.ourservices, name="ourservices"),
]


# Create your views here.
