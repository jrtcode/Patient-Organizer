from django import forms
from .models import (EmergencyContact,DoctorContact,
                    MedicalDoc,Medication)

class EmergencyContactForm(forms.ModelForm):
    class Meta():
        model = EmergencyContact
        fields = '__all__'

class DoctorContactForm(forms.ModelForm):
    class Meta():
        model = DoctorContact
        fields = '__all__'

class MedicationForm(models.ModelForm):
    class Meta():
        model = Medication
        fields = '__all__'

class MedicalDocForm(models.ModelForm):
    class Meta():
        model = MedicalDoc
        fields = '__all__'
