from django.urls import path
from . import views
urlpatterns = [
    path('', views.home,name='home'),
    path('signup/', views.signup,name='register'),
    path('signin/', views.signin, name='signin'),
    path('contact/', views.contact,name='contact'),
    path('about/', views.about,name='about'),
    path('appointments/', views.appointments, name='appointments'),
    path('patient-records/', views.patient_records, name='patient_records'),
    path('services/', views.services, name='services'),
    path('contact/', views.contact, name='contact'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
]
