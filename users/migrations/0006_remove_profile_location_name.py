# Generated by Django 3.1.1 on 2020-12-12 18:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_profile_location_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='location_name',
        ),
    ]
