# Generated by Django 5.0 on 2024-08-27 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academics', '0004_rename_academic_specialization_teachers_academic_specialization'),
    ]

    operations = [
        migrations.AddField(
            model_name='teachers',
            name='job_name',
            field=models.CharField(blank=True, max_length=155, null=True),
        ),
    ]
