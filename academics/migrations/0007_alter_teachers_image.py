# Generated by Django 5.0 on 2024-08-27 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academics', '0006_alter_teachers_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teachers',
            name='image',
            field=models.FileField(blank=True, upload_to='static/images'),
        ),
    ]
