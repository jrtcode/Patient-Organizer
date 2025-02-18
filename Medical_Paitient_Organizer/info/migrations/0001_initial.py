# Generated by Django 3.0.3 on 2020-09-28 18:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import localflavor.us.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Medication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('prescription', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MedicalDoc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('file', models.FileField(upload_to='files/medical-docs')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='EmergencyContact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=16, unique=True)),
                ('alt_phone', models.CharField(blank=True, max_length=16, null=True, unique=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DoctorContact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=12, unique=True)),
                ('fax_phone', models.CharField(blank=True, max_length=12, unique=True)),
                ('address', models.CharField(max_length=1024, verbose_name='address')),
                ('city', models.CharField(default='', max_length=64, verbose_name='city')),
                ('state', localflavor.us.models.USStateField(default='AL', max_length=2, verbose_name='state')),
                ('zip_code', models.CharField(default='', max_length=5, verbose_name='zip code')),
                ('specialty', models.CharField(choices=[('ALLERGY & IMMUNOLOGY', 'ALLERGY & IMMUNOLOGY'), ('ANESTHESIOLOGY', 'ANESTHESIOLOGY'), ('DERMATOLOGY', 'DERMATOLOGY'), ('DIAGNOSTIC RADIOLOGY', 'DIAGNOSTIC RADIOLOGY'), ('EMERGENCY MEDICINE', 'EMERGENCY MEDICINE'), ('FAMILY MEDICINE', 'FAMILY MEDICINE'), ('ITERNAL MEDICINE', 'ITERNAL MEDICINE'), ('MEDICAL GENETICS', 'MEDICAL GENETICS'), ('NEUROLOGY', 'NEUROLOGY'), ('NUCLEAR MEDICINE', 'NUCLEAR MEDICINE'), ('OBSTETRICS AND GYNECOLOGY', 'OBSTETRICS AND GYNECOLOGY'), ('OPHTHALMOLOGY', 'OPHTHALMOLOGY'), ('PATHOLOGY', 'PATHOLOGY'), ('PEDIATRICS', 'PEDIATRICS'), ('PHYSICAL MEDICINE & REHABILITATION', 'PHYSICAL MEDICINE & REHABILITATION'), ('PREVENTIVE MEDICINE', 'PREVENTIVE MEDICINE'), ('PSYCHIATRY', 'PSYCHIATRY'), ('RADIATION ONCOLOGY', 'RADIATION ONCOLOGY'), ('SURGERY', 'SURGERY'), ('UROLOGY', 'UROLOGY')], default='AI', max_length=255)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
