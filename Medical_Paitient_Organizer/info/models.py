from django.db import models
from django.utils.translation import ugettext as ut
from localflavor.us.models import USStateField
from accounts.models import User

# Create your models here.
class EmergencyContact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    phone = models.CharField(unique=True, max_length=16)
    alt_phone = models.CharField(unique=True, max_length=16, blank=True)

    def __str__(self):
        return self.first_name



class DoctorContact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    phone = models.CharField(unique=True, max_length=12)
    fax_phone = models.CharField(unique=True, max_length=12, blank=True)
    address = models.CharField(ut('address'),max_length=1024)
    city = models.CharField(ut('city'),max_length=64, default='')
    state = USStateField(ut("state"), default="AL")
    zip_code = models.CharField(ut("zip code"), max_length=5, default="")

    def __str__(self):
        return f"Dr. {self.first_name} {self.last_name}"


class Medication(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=260)
    prescription = models.TextField()

    def __str__(self):
        return self.name


class MedicalDoc(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    file = models.FileField(upload_to='files/medical-docs')

    def __str__(self):
        return self.file
