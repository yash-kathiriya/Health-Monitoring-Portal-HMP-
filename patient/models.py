from django.db import models
from django.contrib import messages
from django.shortcuts import render, redirect
from django.utils import timezone

class Patient(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]
    
    MARITAL_STATUS_CHOICES = [
        ('Single', 'Single'),
        ('Married', 'Married'),
        ('Divorced', 'Divorced'),
        ('Widowed', 'Widowed'),
    ]
    
    
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES,blank=False, null=True)
    marital_status = models.CharField(max_length=10, choices=MARITAL_STATUS_CHOICES, blank=True, null=True)
    address = models.TextField()
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    username = models.CharField(max_length=150,unique=True)
    password = models.CharField(max_length=128)  # Note: Use Django's built-in user system ideally

    def __str__(self):
        return f"{self.first_name}-{self.middle_name}-{self.last_name}-{self.age}-{self.gender}-{self.marital_status}-{self.address}-{self.phone}-{self.email}-{self.username}-{self.password}"
    
    
class Appointment(models.Model):
    fname = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    date = models.DateField()
    message = models.TextField(blank=True)

    def __str__(self):
        return f"{self.fname} - {self.email} - {self.phone} - {self.date} - {self.message}"
    
    
    
class MedicalRecord(models.Model):
    email = models.EmailField(blank=False,null=True)
    record_date = models.DateField()
    diagnosis = models.TextField()
    treatment_plan = models.TextField()
    prescription = models.TextField()
    doctor_notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now, blank=True)
    
    def __str__(self):
        return f"Record for {self.email}- {self.record_date}- {self.diagnosis}- {self.treatment_plan}- {self.prescription}- {self.doctor_notes}"

