from django.contrib import admin
from .models import Doctor

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'gender','address', 'phone', 'email', 'username','password','qualification','specialization','experience','license','get_certificate_name', 'get_idproof_name')

    def get_certificate_name(self, obj):
        if obj.certificate:
            return obj.certificate.name.split('/')[-1]
        return '-'
    get_certificate_name.short_description = 'Certificate'

    def get_idproof_name(self, obj):
        if obj.idproof:
            return obj.idproof.name.split('/')[-1]
        return '-'
    get_idproof_name.short_description = 'ID Proof'