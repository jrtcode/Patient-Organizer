from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin

class HomeView(TemplateView,LoginRequiredMixin):
    template_name = 'home.html'
