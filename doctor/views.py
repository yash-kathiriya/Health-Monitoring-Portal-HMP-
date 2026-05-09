from django.shortcuts import render, redirect
from .forms import Doctor  
from django.contrib import messages
from .models import Doctor
from patient.models import Appointment
from django.shortcuts import render, get_object_or_404
from patient.models import Patient, MedicalRecord
from django.utils import timezone
from django.contrib.auth.decorators import login_required




def doctor_registration(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        gender = request.POST.get('gender')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        qualification = request.POST.get('qualification')
        specialization = request.POST.get('specialization')
        experience = request.POST.get('experience')
        license_num = request.POST.get('license')

        certificate = request.FILES.get('certificate')
        idproof = request.FILES.get('idproof')
        
        Doctor.objects.create(
            first_name=first_name,
            last_name=last_name,
            gender=gender,
            address=address,
            phone=phone,
            email=email,
            username=username,
            password=password,
            qualification=qualification,
            specialization=specialization,
            experience=experience,
            license=license_num,
            certificate=certificate,
            idproof=idproof  
        )
        
        return redirect('login') 
        
    return render(request, 'doctor_registration.html')

    
# def login_view(request):
#     if request.method == "POST":
#         username = request.POST.get("username")
#         password = request.POST.get("password")

#         patient = Doctor.objects.filter(username__iexact=username, password=password).first()

#         if patient:
#             request.session['user_type'] = 'patient'
#             request.session['user_id'] = patient.id
#             return redirect('about')  # ✅ redirect after login
#         else:
#             messages.error(request, "Invalid username or password")
#             return redirect('login')  # ✅ redirect using URL name

#     return render(request, 'login.html')

def doctor_dashbord(request):
    return render(request,'doctor_dashbord.html')


# views.py

def appointment_list(request):
    today = timezone.now().date()

    # Only appointments with gmail emails
    appointments = Appointment.objects.filter(email__icontains='@gmail.com',date=today)
    return render(request, 'view_appointment.html', {'appointments': appointments})

def viewrecord(request):
    email = request.GET.get("email")
    records = MedicalRecord.objects.filter(email=email)
    return render(request, "view_record.html", {"records": records})





# Doctor profile page
def doctor_profile(request):
    doctor_id = request.session.get('user_id')
    if not doctor_id:
        return redirect('login')  # if not logged in, redirect
    
    doctor = get_object_or_404(Doctor, id=doctor_id)
    return render(request, "doctor_profile.html", {"doctor": doctor})


# Doctor profile update
def dupdate_profile(request):
    doctor_id = request.session.get("user_id")

    if not doctor_id:
        messages.error(request, "Please login first.")
        return redirect("login")

    doctor = get_object_or_404(Doctor, id=doctor_id)

    if request.method == "POST":
        # Update doctor fields
        doctor.first_name = request.POST.get('first_name')
        doctor.last_name = request.POST.get('last_name')
        doctor.gender = request.POST.get('gender')
        doctor.address = request.POST.get('address')
        doctor.phone = request.POST.get('phone')
        doctor.email = request.POST.get('email')
        doctor.username = request.POST.get('username')
        doctor.qualification = request.POST.get('qualification')
        doctor.specialization = request.POST.get('specialization')
        doctor.experience = request.POST.get('experience')
        doctor.license = request.POST.get('license')

        # File uploads (certificate + idproof)
        if request.FILES.get('certificate'):
            doctor.certificate = request.FILES.get('certificate')
        if request.FILES.get('idproof'):
            doctor.idproof = request.FILES.get('idproof')

        # Save changes → updates DB → admin side shows new values
        doctor.save()

        messages.success(request, "Profile updated successfully ✅")
        return redirect("doctor_dashbord")

    return render(request, "doctor_profile.html", {"doctor": doctor})


