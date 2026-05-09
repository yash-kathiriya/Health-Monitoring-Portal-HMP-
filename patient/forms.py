from django import forms
from .models import Appointment
from .models import Patient

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['fname', 'email', 'phone', 'date', 'message']




class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields =['first_name','middle_name', 'last_name','age','gender','marital_status', 'address', 'phone', 'email', 'username','password']
