# Generated by Django 3.2.12 on 2022-02-14 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Homepage', '0003_alter_doctor_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='profile_pic',
            field=models.ImageField(blank=True, default='/static/assets/img/doctor01.jpg', null=True, upload_to='profile_pic/DoctorProfilePic/'),
        ),
    ]
