# Generated by Django 3.0.3 on 2020-09-26 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0002_auto_20200926_1509'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emergencycontact',
            name='alt_phone',
            field=models.CharField(max_length=16, unique=True),
        ),
        migrations.AlterField(
            model_name='emergencycontact',
            name='phone',
            field=models.CharField(max_length=16, unique=True),
        ),
    ]
