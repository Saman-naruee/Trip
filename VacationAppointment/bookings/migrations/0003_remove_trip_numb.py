# Generated by Django 5.0.6 on 2024-08-03 15:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0002_trip_numb'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trip',
            name='Numb',
        ),
    ]
