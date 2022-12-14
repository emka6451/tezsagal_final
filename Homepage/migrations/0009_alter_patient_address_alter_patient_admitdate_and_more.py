# Generated by Django 4.0.5 on 2022-08-29 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Homepage', '0008_remove_patient_assigneddoctorid_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='address',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='admitDate',
            field=models.DateField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='email',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='mobile',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
