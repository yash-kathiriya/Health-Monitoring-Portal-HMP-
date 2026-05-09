# forms.py
from django import forms
from django.contrib.auth.models import User
from .models import Hospital

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class HospitalForm(forms.ModelForm):
    class Meta:
        model = Hospital
        exclude = ['user', 'created_at']
