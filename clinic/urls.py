from django.urls import path
from . import views
urlpatterns = [
    path('', views.home,name='home'),
    path('contact/', views.contact,name='contact'),
    path('about/', views.about,name='about'),
    path('appointments/', views.appointments, name='appointments'),
    path('patient-records/', views.patient_records, name='patient_records'),
    path('services/', views.services, name='services'),
    path('contact/', views.contact, name='contact'),
]
