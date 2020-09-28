from django.db import models
from django.utils.translation import ugettext as ut
from localflavor.us.models import USStateField
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
DOC_SPECIALTY = [
    ('ALLERGY & IMMUNOLOGY','ALLERGY & IMMUNOLOGY'),
    ('ANESTHESIOLOGY','ANESTHESIOLOGY'),
    ('DERMATOLOGY','DERMATOLOGY'),
    ('DIAGNOSTIC RADIOLOGY','DIAGNOSTIC RADIOLOGY'),
    ('EMERGENCY MEDICINE','EMERGENCY MEDICINE'),
    ('FAMILY MEDICINE','FAMILY MEDICINE'),
    ('ITERNAL MEDICINE','ITERNAL MEDICINE'),
    ('MEDICAL GENETICS','MEDICAL GENETICS'),
    ('NEUROLOGY','NEUROLOGY'),
    ('NUCLEAR MEDICINE','NUCLEAR MEDICINE'),
    ('OBSTETRICS AND GYNECOLOGY','OBSTETRICS AND GYNECOLOGY'),
    ('OPHTHALMOLOGY','OPHTHALMOLOGY'),
    ('PATHOLOGY','PATHOLOGY'),
    ('PEDIATRICS','PEDIATRICS'),
    ('PHYSICAL MEDICINE & REHABILITATION','PHYSICAL MEDICINE & REHABILITATION'),
    ('PREVENTIVE MEDICINE','PREVENTIVE MEDICINE'),
    ('PSYCHIATRY','PSYCHIATRY'),
    ('RADIATION ONCOLOGY','RADIATION ONCOLOGY'),
    ('SURGERY','SURGERY'),
    ('UROLOGY','UROLOGY'),
]

class EmergencyContact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    phone = models.CharField(unique=True, max_length=16)
    alt_phone = models.CharField(unique=True, max_length=16, blank=True, null=True)

    def __str__(self):
        return self.first_name

    def get_absolute_url(self):
        return reverse("info:detail_EMC", kwargs={"pk": self.pk})




class DoctorContact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    phone = models.CharField(unique=True, max_length=12)
    fax_phone = models.CharField(unique=True, max_length=12, blank=True)
    address = models.CharField(ut('address'),max_length=1024)
    city = models.CharField(ut('city'),max_length=64, default='')
    state = USStateField(ut("state"), default="AL")
    zip_code = models.CharField(ut("zip code"), max_length=5, default="")
    specialty = models.CharField(max_length=255,choices=DOC_SPECIALTY, default='AI')

    def __str__(self):
        return f"Dr. {self.first_name} {self.last_name}"

    def get_absolute_url(self):
        return reverse("info:detail_doc", kwargs={"pk": self.pk})



class Medication(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    prescription = models.TextField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("info:detail_med", kwargs={"pk": self.pk})

class MedicalDoc(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to='files/medical-docs')

    def get_absolute_url(self):
        return reverse("info:detail_MedDoc", kwargs={"pk": self.pk})
