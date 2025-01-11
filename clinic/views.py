from django.shortcuts import render,redirect
from .forms import *
from django.contrib import messages


# Create your views here.

def home(request):
    return render(request, 'home.html')

def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            messages.success(request, f"Acount created successfully Login Now! ...")
            return redirect('signin')
        else:
            messages.info(request, f"Something went wrong try again ..")
    else:
        form = SignupForm()
    context = {'form': form}
    return render(request,'signup.html', context)

def signin(request):
    return render(request, 'signin.html')

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')


def appointments(request):
    return render(request, 'appointments.html')

def patient_records(request):
    return render(request, 'patient_records.html')

def services(request):
    return render(request, 'services.html')


