from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')
from django.shortcuts import render

def appointments(request):
    return render(request, 'appointments.html')

def patient_records(request):
    return render(request, 'patient_records.html')

def services(request):
    return render(request, 'services.html')


