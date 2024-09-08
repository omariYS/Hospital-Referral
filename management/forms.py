from django import forms
from .models import Hospital, Doctor, Patient, Referral, Appointment, Referred, Referrer

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['patientid', 'fname', 'lname', 'age', 'gender', 'homeadd', 'phonenumber']

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['medicalid', 'fname', 'lname', 'hospitalid', 'specialization', 'phonenumber', 'email', 'gender']

class HospitalForm(forms.ModelForm):
    class Meta:
        model = Hospital
        fields = ['hospitalid', 'hospitalname', 'address', 'contactno']

class ReferralForm(forms.ModelForm):
    class Meta:
        model = Referral
        fields = ['referralid', 'patientid', 'referrerid', 'referredid', 'referraldate', 'visitationdate', 'referralstatus']

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['appointmentid', 'referralid', 'referralid', 'status', 'notes']

class ReferredForm(forms.ModelForm):
    class Meta:
        model = Referred
        fields = ['referredto', 'doctorid', 'hospitalid']

class ReferrerForm(forms.ModelForm):
    class Meta:
        model = Referrer
        fields = ['referrertype', 'doctorid', 'hospitalid']