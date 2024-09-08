import os
from django.conf import settings
from django.shortcuts import render, redirect
from .models import Patient, Doctor, Hospital, Referral, Appointment, Referred, Referrer
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from .forms import PatientForm, DoctorForm, HospitalForm, ReferralForm, AppointmentForm, ReferredForm, ReferrerForm

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

def manage_patients(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('manage_patients')
    else:
        form = PatientForm()
    
    patients = Patient.objects.all()
    return render(request, 'manage_patients.html', {'form': form, 'patients': patients})

def manage_doctors(request):
    if request.method == 'POST':
        form = DoctorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('manage_doctors')
    else:
        form = DoctorForm()

    doctors = Doctor.objects.all()
    return render(request, 'manage_doctors.html', {'form': form, 'doctors': doctors})

def manage_referrals(request):
    if request.method == 'POST':
        form = ReferralForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('manage_referrals')
    else:
        form = ReferralForm()

    referrals = Referral.objects.all()
    return render(request, 'manage_referrals.html', {'form': form, 'referrals': referrals})

def manage_appointments(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('manage_appointments')
    else:
        form = AppointmentForm()

    appointments = Appointment.objects.all()
    return render(request, 'manage_appointments.html', {'form': form, 'appointments': appointments})

def manage_hospitals(request):
    if request.method == 'POST':
        form = HospitalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('manage_hospitals')
    else:
        form = HospitalForm()

    hospitals = Hospital.objects.all()
    return render(request, 'manage_hospitals.html', {'form': form, 'hospital': hospitals})

def manage_referred(request):
    if request.method == 'POST':
        form = ReferredForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('manage_referred')
    else:
        form = ReferredForm()

    referred = Referred.objects.all()
    return render(request, 'manage_referred.html', {'form': form, 'referred': referred})

def manage_referrer(request):
    if request.method == 'POST':
        form = ReferrerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('manage_referrer')
    else:
        form = ReferrerForm()

    referrer = Referrer.objects.all()
    return render(request, 'manage_referrer.html', {'form': form, 'referrer': referrer})

def add_records(request):
    return render(request, 'add_records.html')

def view_records(request):
    return render(request, 'view_records.html')