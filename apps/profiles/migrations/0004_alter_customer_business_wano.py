# Generated by Django 3.2.9 on 2022-10-03 18:10

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_alter_customer_business_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='business_wano',
            field=models.CharField(blank=True, default=0, max_length=10, null=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '9999999999'. Up to 10 digits allowed.", regex='^\\d{9,10}$')], verbose_name='Business WhatsApp No.'),
        ),
    ]