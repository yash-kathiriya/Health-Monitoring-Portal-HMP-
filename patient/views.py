from django.shortcuts import render, redirect,get_object_or_404
from .forms import Appointment  
from patient.models import Patient
from doctor.models import Doctor
from hospital.models import Hospital
from django.contrib import messages
from django.http import HttpResponse
from .models import MedicalRecord
from django.contrib.auth.decorators import login_required
from reportlab.pdfgen import canvas
from io import BytesIO


from django.core.mail import EmailMessage
from django.conf import settings
from reportlab.pdfgen import canvas
from io import BytesIO
from django.utils.timezone import now


def generate_medical_record_pdf(data):
    buffer = BytesIO()
    p = canvas.Canvas(buffer)
    
    p.setFont("Helvetica-Bold", 16)
    p.drawString(200, 800, "Medical Record Invoice")

    p.setFont("Helvetica", 11)
    y = 750

    for key, value in data.items():
        p.drawString(50, y, f"{key}: {value}")
        y -= 25

    p.drawString(50, y - 20, f"Generated on: {now().strftime('%d-%m-%Y %H:%M')}")

    p.showPage()
    p.save()

    buffer.seek(0)
    return buffer



def patient_registration(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        middle_name = request.POST.get('middle_name')
        last_name = request.POST.get('last_name')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        marital_status = request.POST.get('marital_status')
        address = request.POST.get('message')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')

        Patient.objects.create(
            first_name=first_name,
            middle_name=middle_name,
            last_name=last_name,
            age=int(age),
            gender=gender,
            marital_status=marital_status,
            address=address,
            phone=phone,
            email=email,
            username=username,
            password=password  # ⚠️ hash in production
        )
        return redirect('login')   # ✅ fixed (use URL name)

    return render(request, 'patient_registration.html')


def patient_dashbord(request):
    return render(request, "patient_dashbord.html")




# ✅ Patient Profile
@login_required
def patient_profile(request):
    patient_id = request.session.get('user_id')
    if not patient_id:
        return redirect('login')  # if not logged in, redirect
    
    patient = get_object_or_404(Patient, id=patient_id)
    return render(request, "patient_profile.html", {"patient": patient})


from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils import timezone
from datetime import datetime
from .models import Appointment, Patient  # Ensure your models are imported

def appointment_view(request):
    patient_id = request.session.get('user_id')

    if not patient_id:
        messages.error(request, "Session expired. Please log in again.")
        return redirect('login')

    patient = Patient.objects.get(id=patient_id)

    if request.method == 'POST':
        fname = request.POST.get("first_name")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        date_str = request.POST.get('date')
        message = request.POST.get('message')

        # Basic field validation
        if not (fname and phone and email and date_str and message):
            messages.error(request, "All fields are required.")
            return render(request, 'appointment.html', {"patient": patient})

        # Convert string to date
        try:
            selected_date = datetime.strptime(date_str, "%Y-%m-%d").date()
        except ValueError:
            messages.error(request, "Invalid date format.")
            return render(request, 'appointment.html', {"patient": patient})

        # Check if date is in the past
        today = timezone.now().date()
        if selected_date < today:
            messages.error(request, "You cannot book an appointment for a past date.")
            return render(request, 'appointment.html', {"patient": patient})

        # Check if limit reached
        appointment_count = Appointment.objects.filter(date=selected_date).count()
        if appointment_count >= 50:
            messages.error(request, f"Appointments are full for {selected_date}. Please select another date.")
            return render(request, 'appointment.html', {"patient": patient})

        # Create appointment
        Appointment.objects.create(
            fname=fname,
            email=email,
            phone=phone,
            date=selected_date,
            message=message
        )

        messages.success(request, "Appointment booked successfully.")
        return redirect('patient_dashbord')

    return render(request, 'appointment.html', {"patient": patient})




def update_profile(request):
    # Get current logged in patient ID from session
    patient_id = request.session.get("user_id")

    if not patient_id:
        messages.error(request, "Please login first.")
        return redirect("login")

    patient = Patient.objects.get(id=patient_id)

    if request.method == "POST":
        # Get all form values
        first_name = request.POST.get("first_name", "").strip()
        middle_name = request.POST.get("middle_name", "").strip()
        last_name = request.POST.get("last_name", "").strip()
        age = request.POST.get("age", "").strip()
        gender = request.POST.get("gender", "").strip()
        marital_status = request.POST.get("marital_status", "").strip()
        address = request.POST.get("address", "").strip()
        phone = request.POST.get("phone", "").strip()
        email = request.POST.get("email", "").strip()
        username = request.POST.get("username", "").strip()

        # Check for empty fields
        if not all([first_name, last_name, age, gender, address, phone, email, username]):
            messages.error(request, "Please fill in all required fields ❌")
            return redirect("update_profile")

        # Optionally, add more specific validation
        if not age.isdigit():
            messages.error(request, "Age must be a number ❌")
            return redirect("update_profile")

        if len(phone) != 10 or not phone.isdigit():
            messages.error(request, "Enter a valid 10-digit phone number ❌")
            return redirect("update_profile")

        # If all validations pass, update patient info
        patient.first_name = first_name
        patient.middle_name = middle_name
        patient.last_name = last_name
        patient.age = age
        patient.gender = gender
        patient.marital_status = marital_status
        patient.address = address
        patient.phone = phone
        patient.email = email
        patient.username = username

        patient.save()

        messages.success(request, "Profile updated successfully ✅")
        return redirect("patient_dashbord")

    return render(request, "patient_profile.html", {"patient": patient})


def add_record(request):
    patient_id = request.session.get("user_id")
    patient = Patient.objects.get(id=patient_id)

    if request.method == "POST":
        email = request.POST.get("email")
        record_date = request.POST.get("record_date")
        diagnosis = request.POST.get("diagnosis")
        treatment_plan = request.POST.get("treatment_plan")
        prescription = request.POST.get("prescription")
        doctor_notes = request.POST.get("doctor_notes")

        # find patient by email
        patient = Patient.objects.filter(email=email).first()
        if not patient:
            messages.error(request, "Patient with this email not found!")
            return redirect("view_appointment")

        # save record
        record = MedicalRecord.objects.create(
            email=email,
            record_date=record_date,
            diagnosis=diagnosis,
            treatment_plan=treatment_plan,
            prescription=prescription,
            doctor_notes=doctor_notes
        )

        # PDF data
        pdf_data = {
            "Patient Email": email,
            "Record Date": record_date,
            "Diagnosis": diagnosis,
            "Treatment Plan": treatment_plan,
            "Prescription": prescription,
            "Doctor Notes": doctor_notes,
        }

        pdf_file = generate_medical_record_pdf(pdf_data)
        email_body = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Medical Record</title>
</head>
<body style="margin:0; padding:0; background-color:#f4f6f8; font-family:Arial, sans-serif;">

    <table align="center" width="100%" cellpadding="0" cellspacing="0">
        <tr>
            <td align="center">
                <table width="600" cellpadding="0" cellspacing="0" 
                       style="background-color:#ffffff; margin-top:30px; border-radius:10px; overflow:hidden; box-shadow:0 4px 10px rgba(0,0,0,0.1);">

                    <!-- HEADER -->
                    <tr>
                        <td style="background-color:#0d6efd; padding:20px; text-align:center;">
                            <h1 style="color:#ffffff; margin:0;">🏥 Health Monitoring Portal</h1>
                            <p style="color:#e0e0e0; margin:5px 0 0;">Your Health, Our Priority</p>
                        </td>
                    </tr>

                    <!-- BODY -->
                    <tr>
                        <td style="padding:30px;">
                            <h2 style="color:#333;">Hello Patient,</h2>
                            <p style="color:#555; line-height:1.6;">
                                Your medical record has been successfully created.
                                Please find the attached PDF containing your medical details.
                            </p>

                            <table width="100%" cellpadding="8" cellspacing="0" 
                                   style="border-collapse:collapse; margin-top:20px;">
                                <tr style="background-color:#f1f1f1;">
                                    <td><strong>Email</strong></td>
                                    <td>{email}</td>
                                </tr>
                                <tr>
                                    <td><strong>Record Date</strong></td>
                                    <td>{record_date}</td>
                                </tr>
                                <tr style="background-color:#f1f1f1;">
                                    <td><strong>Diagnosis</strong></td>
                                    <td>{diagnosis}</td>
                                </tr>
                                <tr>
                                    <td><strong>Treatment Plan</strong></td>
                                    <td>{treatment_plan}</td>
                                </tr>
                            </table>

                            <p style="margin-top:25px; color:#555;">
                                If you have any questions, feel free to contact us.
                            </p>

                            <p style="margin-top:20px;">
                                <strong>Stay Healthy,</strong><br>
                                Health Monitoring Portal Team
                            </p>
                        </td>
                    </tr>

                    <!-- FOOTER -->
                    <tr>
                        <td style="background-color:#f8f9fa; padding:15px; text-align:center; font-size:12px; color:#777;">
                            © 2025 Health Monitoring Portal | Confidential Medical Information
                        </td>
                    </tr>

                </table>
            </td>
        </tr>
    </table>

</body>
</html>
"""

        # send email with pdf
        mail = EmailMessage(
        subject="Your Medical Record - Health Monitoring Portal",
        body=email_body,
        from_email=settings.EMAIL_HOST_USER,
        to=[email],
        )
        mail.content_subtype = "html"  # IMPORTANT
        mail.attach("medical_record.pdf", pdf_file.read(), "application/pdf")
        mail.send()

        # delete appointment
        Appointment.objects.filter(email=email).delete()

        messages.success(request, "Medical Record saved & emailed successfully!")
        return redirect("view_appointment")

    return render(request, "add_record.html", {"patient": patient})


def record(request):
    patient_id = request.session.get('user_id')
    patient = Patient.objects.get(id=patient_id)
    email = patient.email

    # Check if appointment exists for this email
    if MedicalRecord.objects.filter(email=email).exists():
        records = MedicalRecord.objects.filter(email=email)
    else:
        records = []  # no records if no appointment

    return render(request, "record.html", {"records": records})

