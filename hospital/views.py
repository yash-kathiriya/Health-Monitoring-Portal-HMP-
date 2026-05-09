# views.py
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.models import User
from .forms import Hospital
from django.contrib import messages
from .models import Hospital

def patient_registration_by_hospital(request):
    return render(request,"hospital_patient_reg.html")


def patient_registration(request):
    if request.method == 'POST':
        name = request.POST.get('first_name')
        address = request.POST.get('address')
        city = request.POST.get('city')
        state=request.POST.get('state')
        pincode = request.POST.get('pincode')
        registration_number = request.POST.get('registration_number')
        established_year = request.POST.get('established_year')
        phone = request.POST.get('phone'),
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Save the record manually
        Hospital.objects.create(
            name=name,
            address=address,
            city=city,
            state=state,
            pincode=pincode,
            registration_number=registration_number,
            established_year=established_year,
            phone=phone,
            email=email,
            username=username,
            password=password  # In production, hash this!
        )
        return redirect('login')  # Make sure this URL/view exists

    return render(request, 'hospital_registration.html')


def about(request):
    return render(request,'about.html')

def hospital_dashbord(request):
    return render(request,'hospital_dashbord.html')


def hospital_profile(request):
    hospital_id = request.session.get("user_id")  # assuming you store logged-in hospital id in session
    if not hospital_id:
        return redirect("login")

    hospital = get_object_or_404(Hospital, id=hospital_id)
    return render(request, "hospital_profile.html", {"hospital": hospital})


def update_hospital_profile(request):
    hospital_id = request.session.get("user_id")
    if not hospital_id:
        return redirect("login")

    hospital = get_object_or_404(Hospital, id=hospital_id)

    if request.method == "POST":
        hospital.name = request.POST.get("first_name")
        hospital.address = request.POST.get("address")
        hospital.city = request.POST.get("city")
        hospital.state = request.POST.get("state")
        hospital.pincode = request.POST.get("pincode")
        hospital.registration_number = request.POST.get("registration_number")
        hospital.established_year = request.POST.get("established_year")
        hospital.phone = request.POST.get("phone")
        hospital.email = request.POST.get("email")
        hospital.username = request.POST.get("username")

        # ✅ if password field exists and user wants to change it
        if request.POST.get("password"):
            hospital.password = request.POST.get("password")  # ⚠️ hash in production!

        hospital.save()

        messages.success(request, "Profile updated successfully ✅")
        return redirect("hospital_dashbord")

    return render(request, "hospital_profile.html", {"hospital": hospital})
