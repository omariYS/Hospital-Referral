from django.contrib import admin
from .models import Hospital, Doctor, Patient, Referral, Appointment, Referrer, Referred


admin.site.register(Hospital)
admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Referral)
admin.site.register(Appointment)
admin.site.register(Referrer)
admin.site.register(Referred)

