from django.urls import path
from . import views

app_name = 'info'

urlpatterns = [
    path('create/EM-contact', views.EmergencyContactCreateView.as_view(),name='create_EMC'),
    path('', views.EmergencyContactListView.as_view(),name='info'),
    path('EM-contact/<int:pk>/update', views.EmergencyContactUpdateView.as_view(), name='update_EMC'),
    path('EM-contact/<int:pk>/delete/confirm-delete', views.EmergencyContactDeleteView.as_view(), name='delete_EMC'),
    path('EM-contact/<int:pk>', views.EmergencyContactDetailView.as_view(),name='detail_EMC'),
    path('create/Doc-contact', views.DoctorContactCreateView.as_view(),name='create_doc'),
    path('Doctors/', views.DoctorContactListView.as_view(),name='doc_list'),
    path('Doc-contact/<int:pk>', views.DoctorContactDetailView.as_view(),name='detail_doc'),
    path('Doc-contact/<int:pk>/update', views.DoctorContactUpdateView.as_view(), name='update_doc'),
    path('Doc-contact/<int:pk>/delete/confirm-delete', views.DoctorContactDeleteView.as_view(), name='delete_doc'),
    path('create/Medication', views.MedicationCreateView.as_view(),name='create_med'),
    path('Medications/', views.MedicationListView.as_view(),name='med_list'),
    path('Medication/<int:pk>', views.MedicationDetailView.as_view(),name='detail_med'),
    path('Medication/<int:pk>/update', views.MedicationUpdateView.as_view(), name='update_med'),
    path('Medication/<int:pk>/delete/confirm-delete', views.MedicationDeleteView.as_view(), name='delete_med'),
]
