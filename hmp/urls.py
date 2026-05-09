"""
URL configuration for hmp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
  
    path('admin/', admin.site.urls),
    
    path('', views.home, name='home'),
    path('registration/', views.registration, name='registration'),
    path('', include('patient.urls'), name='patient_registration'),
    path('', include('doctor.urls'), name='doctor_registration'),
    path('', include('hospital.urls'), name='hospital_registration'),
    path('login/', views.login_view, name='login'),
    path('',include('patient.urls'),name='appointment'),
    path('',include('hospital.urls'),name='about'),
    path('success/', views.success, name='success'),
    path('',include('patient.urls'),name='patient_dashbord'),
    path('',include('patient.urls'),name='record'),
    path('', include('doctor.urls'), name='view_appointment'),
    path('', include('doctor.urls'), name='view_record'),
    path('', include('patient.urls'), name="view_p_record"),
    path("", include('patient.urls'), name="patient_profile"),
    path('', include('patient.urls'), name='update_profile'),
    path("", include('doctor.urls'), name="doctor_profile"),
    path("", include('doctor.urls'), name="dupdate_profile"),
    path('', include('hospital.urls'), name='hospital_dashbord'),
    path("", include('hospital.urls'), name="hospital_profile"),
    path("", include('hospital.urls'), name="update_hospital_profile"),
    path("", include('patient.urls'), name="add_record"),
    # path('', include('patient.urls'), name='viewrecord'),
    path('', include('hospital.urls'), name='patient_registration_by_hospital'),
    path("", include('doctor.urls'), name="patient_record"),   
    path('check-email/', views.check_email, name='check_email'),
    path('check-appointment-limit/', views.check_appointment_limit, name='check_appointment_limit'),
    
]
