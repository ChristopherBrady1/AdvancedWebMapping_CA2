# Generated by Django 3.1.1 on 2020-12-12 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profile_location_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='location_name',
            field=models.CharField(default=None, max_length=100, null=True),
        ),
    ]
