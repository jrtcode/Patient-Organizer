from django.urls import path
from . import views

app_name = 'info'

urlpatterns = [
    path('create/EM-contact', views.EmergencyContactCreateView.as_view(),name='create_EMC'),
    path('', views.EmergencyContactListView.as_view(),name='info'),
]
