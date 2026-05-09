from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib import messages
from patient.models import Patient
from doctor.models import Doctor
from hospital.models import Hospital
from django.http import JsonResponse
from django.views.decorators.http import require_GET
from patient.models import Appointment  # use your actual model name
from datetime import datetime

def check_appointment_limit(request):
    date_str = request.GET.get('date')
    try:
        selected_date = datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError:
        return JsonResponse({'error': 'Invalid date format'}, status=400)

    count = Appointment.objects.filter(date=selected_date).count()
    if count >= 50:
        return JsonResponse({'full': True})
    return JsonResponse({'full': False})


def home(request):
    return render(request,'index.html')

def registration(request):
    return render(request,'registration.html')

def patient_registration(request):
    return render(request,'patient_registration.html')

def doctor_registration(request):
    return render(request,'doctor_registration.html')

def hospital_registration(request):
    return render(request,'hospital_registration.html')

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        # case-insensitive username, direct password match
        patient = Patient.objects.filter(username__iexact=username, password=password).first()
        doctor = Doctor.objects.filter(username__iexact=username, password=password).first()
        hospital = Hospital.objects.filter(username__iexact=username, password=password).first()
        
        if patient:
            request.session['user_type'] = 'Patient'
            request.session['user_id'] = patient.id
            return redirect('patient_dashbord')  
        elif doctor:
            request.session['user_type'] = 'Doctor'
            request.session['user_id'] = doctor.id
            return redirect('doctor_dashbord')  
        elif hospital:
            request.session['user_type'] = 'Hospital'
            request.session['user_id'] = hospital.id
            return redirect('hospital_dashbord')  
        else:
            messages.error(request, "Invalid username or password")
            return redirect('login')

    return render(request, 'login.html')

def appointment(request):
    return render(request, 'appointment.html')

def about(request):
    return render(request,'about.html')

def success(request):
    return render(request, 'success.html')

def patient_dashbord(request):
    return render(request,'patient_dashbord.html')




def hospital_registration_patient(request):
    return render(request,'hospital_patient_reg.html')



@require_GET
def check_email(request):
    email = request.GET.get('email', '')
    exists = Doctor.objects.filter(email=email).exists()
    return JsonResponse({'exists': exists})
    


