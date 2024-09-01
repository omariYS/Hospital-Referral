from django.db import models

# Create Models/Record forms
class Student(models.Model):
    COURSES = [ #This list will appear as a dropwdown options to select from
        ('AI', 'Professional Diploma in Artificial Intelligence'),
        ('IT', 'Professional Diploma in Data Analytics'),
        ('ECE', 'Professional Diploma in Software Engineering'),
        ('ME', 'Professional Diploma in Blockchain Technology'),
    ]
    
    student_id = models.CharField(max_length=150, unique=True)#'unique' means whatever record your entered cannot be duplicated by another record
    names = models.CharField(max_length=150)
    course = models.CharField(max_length=10, choices=COURSES) #"choices" will take the options of the list above
    email_address = models.CharField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=15, unique=True, null=True, blank=True)#'null' means the field can be empty in the database and 'blank' means the field can be empty in the form

class Meta:
    verbose_name_plural = 'Student List'

    def __str__(self):
        return self.names


class Attendance(models.Model):
    studentID = models.CharField(max_length=50, unique=False)
    date = models.DateTimeField(unique=True)
    studentName = models.CharField(max_length=100, unique=True)

class Meta:
    verbose_name_plural = 'Student Attendance'

    def __str__(self):
        return self.studentID