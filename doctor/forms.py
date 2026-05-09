from django import forms
from .models import Doctor

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields =['first_name', 'last_name','gender','address', 'phone', 'email', 'username','password','qualification','specialization','experience','license','certificate','idproof']
