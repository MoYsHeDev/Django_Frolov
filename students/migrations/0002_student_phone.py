# Generated by Django 3.2.6 on 2021-09-01 06:09

from django.db import migrations

import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(default=None, max_length=128, region=None,
                                                                 unique=True),
        ),
    ]
