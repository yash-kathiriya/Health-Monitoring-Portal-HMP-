from django.urls import path
from . import views

urlpatterns = [
    path('doctor/', views.doctor_registration, name='doctor_registration'),
    # path('login/', views.login_view, name='login'),
    path('doctor_dashbord/', views.doctor_dashbord, name='doctor_dashbord'),
    path('view_appointment/', views.appointment_list, name='view_appointment'),
    
    path("dprofile/", views.doctor_profile, name="doctor_profile"),
    path("dprofile/update/", views.dupdate_profile, name="dupdate_profile"),
    path("patient_record/", views.viewrecord, name="patient_record"),

   
]


