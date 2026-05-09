from django.urls import path
from . import views

urlpatterns = [
    path('appointment/', views.appointment_view, name='appointment'),
    path('patient/', views.patient_registration, name='patient_registration'),
    # path('login/', views.login_view, name='login'),
    path('patient_dashbord/', views.patient_dashbord, name='patient_dashbord'),
   
   path('view_p_record/', views.record, name='view_p_record'),

    path("add_record/", views.add_record, name="add_record"),
    path("profile/", views.patient_profile, name="patient_profile"),
     path("profile/update/", views.update_profile, name="update_profile"),

]


