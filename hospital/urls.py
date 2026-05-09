from django.urls import path, include
from . import views

urlpatterns = [
    path('hospital/', views.patient_registration, name='hospital_registration'),
    path('about/',views.about,name='about'),
    path('hospital_dashbord/', views.hospital_dashbord, name='hospital_dashbord'),
    path("hprofile/", views.hospital_profile, name="hospital_profile"),
    path("hprofile/update/", views.update_hospital_profile, name="update_hospital_profile"),
    path("patient_registration_by_hospital/", views.patient_registration_by_hospital, name="patient_registration_by_hospital")
    
]   


