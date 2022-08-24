# Generated by Django 3.2.9 on 2022-08-24 04:54

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='mobile',
            field=models.CharField(blank=True, max_length=13, null=True, unique=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+919999999999'. Up to 12 digits allowed.", regex='^\\+?91?\\d{9,12}$')], verbose_name='Mobile No'),
        ),
    ]
