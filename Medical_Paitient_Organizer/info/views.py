from django.shortcuts import render
from django.views.generic import (TemplateView,CreateView, DeleteView,
                                ListView, UpdateView, DetailView,)
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from .models import EmergencyContact
from django.urls import reverse_lazy

# Create your views here.

class EmergencyContactCreateView(CreateView,LoginRequiredMixin):
    template_name = 'info/create_EMC.html'
    model = EmergencyContact
    fields = ['first_name', 'last_name', 'phone', 'alt_phone']
    success_url = reverse_lazy('info:info')

class EmergencyContactListView(ListView,LoginRequiredMixin):
    template_name = 'info/EmergencyContact_list.html'
    model = EmergencyContact
    queryset = EmergencyContact.objects.all()
