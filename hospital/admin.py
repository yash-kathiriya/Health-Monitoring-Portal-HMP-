from django.contrib import admin
from .models import Hospital

@admin.register(Hospital)
class HospitalAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'address',
        'city',
        'state',
        'pincode',
        'registration_number',
        'established_year',
        'phone',
        'email',
        'username',
        'password',
    )
