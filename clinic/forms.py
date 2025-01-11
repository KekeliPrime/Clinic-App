from django import forms  
from django.contrib.auth.forms import UserCreationForm 
from django.forms import ModelForm
from django import forms
from .models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User



class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = [ 'full_name',  'phone_number', 'student_id',  'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter username', 'autocomplete': 'off'}),
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter full name'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter phone number'}),
            'student_id': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter student ID'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter address'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter email', 'autocomplete': 'off'}),
        }
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter password', 'autocomplete': 'off'})
    )
    password2 = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm password', 'autocomplete': 'off'})
    )

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email and User.objects.filter(email=email).exists():
            raise forms.ValidationError('This email is already in use! Try another email.')
        return email

    def clean_student_id(self):
        student_id = self.cleaned_data.get('student_id')
        if student_id and User.objects.filter(student_id=student_id).exists():
            raise forms.ValidationError('This student ID is already in use! Try another student ID.')
        return student_id
