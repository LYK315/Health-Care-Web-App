from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('find-a-doctor/', views.findadoctor, name="find-a-doctor"),
    path('register/', views.register, name="register"),
    path('postRegister/', views.postRegister, name="postRegister"),
    path('postLogin/', views.postLogin, name="postLogin"),
    path('logout/', views.logout, name='logout'),
    path('specialty/', views.specialty, name="specialty"),
    path('healthcare-blog/', views.healthcareblog, name="healthcare-blog"),
    path('our-services/', views.ourservices, name="our-services"),
    path('enquiry/', views.enquiry, name="enquiry"),
    path('about-us/', views.aboutus, name="about-us"),
    path('doctors-information/', views.doctorsInformation, name="doctors-information"),
    path('make-appointment/', views.makeAppointment, name="make-appointment"),
]
