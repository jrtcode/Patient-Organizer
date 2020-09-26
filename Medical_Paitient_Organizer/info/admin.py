from django.contrib import admin
from .models import (EmergencyContact,Medication,
                    DoctorContact,MedicalDoc)

# Register your models here.
admin.site.register(EmergencyContact)
admin.site.register(MedicalDoc)
admin.site.register(Medication)
admin.site.register(DoctorContact)
