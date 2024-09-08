from django.urls import path
from .views import index, home, patient_list, doctor_list, hospital_list, referral_list, appointment_list, register, CustomLoginView, logout, manage_patients, manage_doctors, manage_referrals, manage_appointments, manage_hospitals, add_records, view_records, manage_referred, manage_referrer


urlpatterns = [
    path('', index, name='index'),
    path('patients/', manage_patients, name='manage_patients'),
    path('doctors/', manage_doctors, name='manage_doctors'),
    path('referrals/', manage_referrals, name='manage_referrals'),
    path('appointments/', manage_appointments, name='manage_appointments'),
    path('hospitals/', manage_hospitals, name='manage_hospitals'),
    path('register/', register, name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', logout, name='logout'),
    path('index/', home, name='home'),
    path('patients_list/', patient_list, name='patient_list'),
    path('doctor_list/', doctor_list, name='doctor_list'),
    path('hospital_list/', hospital_list, name='hospital_list'),
    path('referral_list/', referral_list, name='referral_list'),
    path('appointment_list  /', appointment_list, name='appointment_list'),
    path('add_records/', add_records, name='add_records'),
    path('view_records/', view_records, name='view_records'),
    path('referred/', manage_referred, name='manage_referred'),
    path('referrer/', manage_referrer, name='manage_referrer'),
]