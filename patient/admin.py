from django.contrib import admin
from .models import Patient
from .models import Appointment
from .models import MedicalRecord


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('fname', 'email', 'phone', 'date', 'message')
    
    
    
@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('first_name','middle_name', 'last_name','age','gender','marital_status', 'address', 'phone', 'email', 'username','password')
    

    
@admin.register(MedicalRecord)
class MedicalRecordAdmin(admin.ModelAdmin):
    list_display = ('email', 'record_date', 'diagnosis','treatment_plan','prescription','doctor_notes')
     