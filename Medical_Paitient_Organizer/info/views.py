from django.shortcuts import render
from django.views.generic import (TemplateView,CreateView, DeleteView,
                                ListView, UpdateView, DetailView,)
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from .models import (EmergencyContact, DoctorContact,
                    Medication,MedicalDoc)
from .forms import (EmergencyContactForm, DoctorContactForm,
                    MedicationForm,MedicalDocForm)
from django.urls import reverse_lazy

# Create your views here.

class EmergencyContactCreateView(CreateView,LoginRequiredMixin):
    template_name = 'info/create_EMC.html'
    form_class = EmergencyContactForm
    success_url = reverse_lazy('info:info')

class EmergencyContactDetailView(DetailView,LoginRequiredMixin):
    model = EmergencyContact
    template_name = 'info/EmergencyContact_detail.html'

class EmergencyContactListView(ListView,LoginRequiredMixin):
    template_name = 'info/EmergencyContact_list.html'
    model = EmergencyContact
    queryset = EmergencyContact.objects.all()

class EmergencyContactUpdateView(UpdateView,LoginRequiredMixin):
    template_name_suffix = '_update_form'
    form_class = EmergencyContactForm
    model = EmergencyContact

class EmergencyContactDeleteView(DeleteView,LoginRequiredMixin):
    model = EmergencyContact
    success_url = reverse_lazy('info:info')

class DoctorContactCreateView(CreateView, LoginRequiredMixin):
    template_name = 'info/create_DoctorContact.html'
    form_class = DoctorContactForm
    success_url = reverse_lazy('info:doc_list')

class DoctorContactListView(ListView, LoginRequiredMixin):
    template_name = 'info/DoctorContact_list.html'
    model = DoctorContact
    queryset = DoctorContact.objects.all()

class DoctorContactDetailView(DetailView,LoginRequiredMixin):
    model = DoctorContact
    template_name = 'info/DoctorContact_detail.html'

class DoctorContactDeleteView(DeleteView,LoginRequiredMixin):
    model = DoctorContact
    success_url = reverse_lazy('info:doc_list')

class DoctorContactUpdateView(UpdateView,LoginRequiredMixin):
    template_name_suffix = '_update_form'
    model = DoctorContact
    form_class = DoctorContactForm

class MedicationCreateView(CreateView, LoginRequiredMixin):
    template_name = 'info/create_Medication.html'
    form_class = MedicationForm
    success_url = reverse_lazy('info:med_list')

class MedicationListView(ListView, LoginRequiredMixin):
    template_name = 'info/Medication_list.html'
    model = Medication
    queryset = Medication.objects.all()

class MedicationDetailView(DetailView,LoginRequiredMixin):
    model = Medication
    template_name = 'info/Medication_detail.html'

class MedicationDeleteView(DeleteView,LoginRequiredMixin):
    model = Medication
    success_url = reverse_lazy('info:med_list')

class MedicationUpdateView(UpdateView,LoginRequiredMixin):
    template_name_suffix = '_update_form'
    model = Medication
    form_class = MedicationForm

class MedicalDocListView(ListView, LoginRequiredMixin):
    template_name = 'info/MedicalDoc_list.html'
    model = MedicalDoc
    context_object_name = 'MedDoc'
    queryset = MedicalDoc.objects.all()

class MedicalDocDetailView(DetailView,LoginRequiredMixin):
    model = MedicalDoc
    template_name = 'info/MedicalDoc_detail.html'

class MedicalDocDeleteView(DeleteView,LoginRequiredMixin):
    model = MedicalDoc
    success_url = reverse_lazy('info:MedDoc_list')

class MedicalDocUpdateView(UpdateView,LoginRequiredMixin):
    template_name_suffix = '_update_form'
    model = MedicalDoc
    form_class = MedicalDocForm

class MedicalDocCreateView(CreateView,LoginRequiredMixin):
    template_name = 'info/create_MedicalDoc.html'
    form_class = MedicalDocForm
    success_url = reverse_lazy('info:MedDoc_list')
