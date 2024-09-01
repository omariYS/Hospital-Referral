import os
from django.conf import settings
from django.shortcuts import render, redirect
from .models import Patient, Doctor, Hospital, Referral, Appointment
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy

# User registration view
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


class CustomLoginView(LoginView):
    template_name = 'login.html'

def logout(request):
    return render(request, 'logout.html')

def home(request):
    return render(request, 'index.html')

def index(request):
    return render(request, 'home.html')

def patient_list(request):
    patients = Patient.objects.all()
    return render(request, 'patients.html', {'patients': patients})

def doctor_list(request):
    doctors = Doctor.objects.all()
    return render(request, 'doctors.html', {'doctors': doctors})

def hospital_list(request):
    hospitals = Hospital.objects.all()
    return render(request, 'hospitals.html', {'hospitals': hospitals})

def referral_list(request):
    referrals = Referral.objects.all()
    return render(request, 'referrals.html', {'referrals': referrals})

def appointment_list(request):
    appointments = Appointment.objects.all()
    return render(request, 'appointments.html', {'appointments': appointments})