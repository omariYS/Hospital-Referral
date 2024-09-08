# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Appointment(models.Model):
    entryid = models.AutoField(db_column='EntryID', primary_key=True)  # Field name made lowercase.
    appointmentid = models.CharField(db_column='AppointmentID', unique=True, max_length=255)  # Field name made lowercase.
    referralid = models.ForeignKey('Referral', models.DO_NOTHING, db_column='ReferralID')  # Field name made lowercase.
    appointmentdate = models.DateTimeField(db_column='AppointmentDate')  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=9, blank=True, null=True)  # Field name made lowercase.
    notes = models.TextField(db_column='Notes', blank=True, null=True)  # Field name made lowercase

    class Meta:
        managed = False
        db_table = 'Appointment'
        verbose_name_plural = 'Appointments Record'

    def __str__(self):
        return self.appointmentid


class Doctor(models.Model):
    entryid = models.AutoField(db_column='EntryID', primary_key=True)  # Field name made lowercase.
    medicalid = models.CharField(db_column='MedicalID', unique=True, max_length=255)  # Field name made lowercase.
    fname = models.CharField(db_column='FName', max_length=255)  # Field name made lowercase.
    lname = models.CharField(db_column='LName', max_length=255)  # Field name made lowercase.
    hospitalid = models.ForeignKey('Hospital', models.DO_NOTHING, db_column='HospitalID', blank=True, null=True)  # Field name made lowercase.
    specialization = models.CharField(db_column='Specialization', max_length=255, blank=True, null=True)  # Field name made lowercase.
    phonenumber = models.CharField(db_column='PhoneNumber', unique=True, max_length=20)  # Field name made lowercase.
    email = models.CharField(db_column='Email', unique=True, max_length=255)  # Field name made lowercase.
    gender = models.CharField(db_column='Gender', max_length=13)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Doctor'
        verbose_name_plural = 'Doctors Record'

    def __str__(self):
        return self.medicalid


class Hospital(models.Model):
    entryid = models.AutoField(db_column='EntryID', primary_key=True)  # Field name made lowercase.
    hospitalid = models.CharField(db_column='HospitalID', unique=True, max_length=255)  # Field name made lowercase.
    hospitalname = models.CharField(db_column='HospitalName', max_length=255)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=255)  # Field name made lowercase.
    contactno = models.CharField(db_column='ContactNo', unique=True, max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Hospital'
        verbose_name_plural = 'Hospitals Record'

    def __str__(self):
        return self.hospitalid


class Patient(models.Model):
    entryid = models.AutoField(db_column='EntryID', primary_key=True)  # Field name made lowercase.
    patientid = models.CharField(db_column='PatientID', unique=True, max_length=255)  # Field name made lowercase.
    fname = models.CharField(db_column='FName', max_length=255)  # Field name made lowercase.
    lname = models.CharField(db_column='LName', max_length=255)  # Field name made lowercase.
    age = models.IntegerField(db_column='Age')  # Field name made lowercase.
    gender = models.CharField(db_column='Gender', max_length=13)  # Field name made lowercase.
    homeadd = models.CharField(db_column='HomeAdd', max_length=255, blank=True, null=True)  # Field name made lowercase.
    phonenumber = models.CharField(db_column='PhoneNumber', unique=True, max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Patient'
        verbose_name_plural = 'Patients Record'

    def __str__(self):
        return self.patientid


class Referral(models.Model):
    entryid = models.AutoField(db_column='EntryID', primary_key=True)  # Field name made lowercase.
    referralid = models.CharField(db_column='ReferralID', unique=True, max_length=255)  # Field name made lowercase.
    patientid = models.ForeignKey(Patient, models.DO_NOTHING, db_column='PatientID')  # Field name made lowercase.
    referrerid = models.ForeignKey('Referrer', models.DO_NOTHING, db_column='ReferrerID')  # Field name made lowercase.
    referredid = models.ForeignKey('Referred', models.DO_NOTHING, db_column='ReferredID')  # Field name made lowercase.
    referraldate = models.DateTimeField(db_column='ReferralDate', blank=True, null=True)  # Field name made lowercase.
    visitationdate = models.DateTimeField(db_column='VisitationDate')  # Field name made lowercase.
    referralstatus = models.CharField(db_column='ReferralStatus', max_length=8, blank=True, null=True)  # Field name made lowercase.
    notes = models.TextField(db_column='Notes', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Referral'
        verbose_name_plural = 'Referrals'

    def __str__(self):
        return self.referralid


class Referred(models.Model):
    entryid = models.AutoField(db_column='EntryID', primary_key=True)  # Field name made lowercase.
    referredto = models.CharField(db_column='ReferredTo', max_length=8)  # Field name made lowercase.
    doctorid = models.ForeignKey(Doctor, models.DO_NOTHING, db_column='DoctorID', blank=True, null=True)  # Field name made lowercase.
    hospitalid = models.ForeignKey(Hospital, models.DO_NOTHING, db_column='HospitalID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Referred'
        verbose_name_plural = 'Referred To'

    def __str__(self):
        return self.referredto


class Referrer(models.Model):
    entryid = models.AutoField(db_column='EntryID', primary_key=True)  # Field name made lowercase.
    referrertype = models.CharField(db_column='ReferrerType', max_length=8)  # Field name made lowercase.
    doctorid = models.ForeignKey(Doctor, models.DO_NOTHING, db_column='DoctorID', blank=True, null=True)  # Field name made lowercase.
    hospitalid = models.ForeignKey(Hospital, models.DO_NOTHING, db_column='HospitalID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Referrer'
        verbose_name_plural = 'Referrer'

    def __str__(self):
        return self.referrertype
