# Generated by Django 5.0 on 2024-08-27 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academics', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='Custom_id',
            field=models.PositiveIntegerField(blank=True, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='teachers',
            name='Custom_id',
            field=models.PositiveIntegerField(blank=True, null=True, unique=True),
        ),
    ]