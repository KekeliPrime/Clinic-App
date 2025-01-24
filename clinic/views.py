from django.shortcuts import render,redirect
from .forms import *
from django.contrib import messages
from .models import User
from django.contrib import messages
from django.conf import settings
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.views.generic.detail import DetailView , BaseDetailView
from django.views.generic import TemplateView, View, UpdateView, ListView, CreateView, DeleteView
from django.contrib.auth import login, logout, authenticate  
from django.utils.encoding import force_bytes, force_str   
from django.contrib.sites.shortcuts import get_current_site  
from django.template.loader import render_to_string 
from django.utils.http import urlsafe_base64_encode , urlsafe_base64_decode  
from django.core.mail import EmailMessage, EmailMultiAlternatives   
from .models import User
from django.contrib.auth import get_user_model 
from django.contrib.auth.hashers import make_password
from django.contrib.auth.views import LoginView, PasswordResetView
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
UserModel = get_user_model()
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist
from .forms import *
from django.dispatch import receiver
from django.utils import timezone
from django.core.paginator import Paginator
from django.db import DatabaseError
from django.core.exceptions import ValidationError



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
    if request.user.is_authenticated:
        next = request.META.get("HTTP_REFERER")
        return redirect(next)
    if request.method == "POST":
       
       student_id = request.POST['student_id']
       password = request.POST['password']
       try:
         
         if User.objects.filter(student_id=student_id,password=password).exists(): 
            target_user = User.objects.get(student_id=student_id)
            user_one = authenticate(request,username=student_id, password=password)
            if user_one is not None:
              login(user_one)
              messages.success(request, f"Logged in Succesfull")
              return redirect("admin_dashboard")
         else:
            messages.info(request, f"Something went wrong")
            return redirect(request.META.get("HTTP_REFERER"))
       except:
        User.DoesNotExist()
        messages.info(request, f"account not found register now")
        
    
    return render(request, 'signin.html')


def admin_dashboard(request):
    if not request.user.is_admin or request.user.is_sammykeys:
        return redirect("signin")
    return render(request, 'admin_dashboard.html')

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


