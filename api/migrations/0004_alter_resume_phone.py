# Generated by Django 4.1.6 on 2023-11-17 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_resume_education_resume_experience_resume_location_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='phone',
            field=models.CharField(max_length=255),
        ),
    ]
