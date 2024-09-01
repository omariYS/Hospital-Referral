from django.urls import path
from .views import index, home, patient_list, doctor_list, hospital_list, referral_list, appointment_list, register, CustomLoginView, logout


urlpatterns = [
    path('', index, name='index'),
    path('patients/', patient_list, name='patient_list'),
    path('doctors/', doctor_list, name='doctor_list'),
    path('hospitals/', hospital_list, name='hospital_list'),
    path('referrals/', referral_list, name='referral_list'),
    path('appointments/', appointment_list, name='appointment_list'),
    path('register/', register, name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', logout, name='logout'),
    path('index/', home, name='home')
]