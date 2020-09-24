from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin

class infoView(TemplateView,LoginRequiredMixin):
    template_name = 'info.html'
