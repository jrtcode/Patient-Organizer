from django.urls import path
from . import views

app_name = 'info'

urlpatterns = [
    path('', views.infoView.as_view(),name='info'),
    path('create/EM-contact', views.EmergencyContactCreateView.as_view(),name='create_EMC'),
]
