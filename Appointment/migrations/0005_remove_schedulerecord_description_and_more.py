# Generated by Django 4.0.5 on 2022-09-08 13:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Appointment', '0004_schedulerecord_description_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schedulerecord',
            name='description',
        ),
        migrations.RemoveField(
            model_name='schedulerecord',
            name='service_name',
        ),
    ]
