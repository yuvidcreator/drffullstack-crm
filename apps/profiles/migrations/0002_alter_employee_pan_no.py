# Generated by Django 3.2.9 on 2022-10-03 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='pan_no',
            field=models.CharField(blank=True, max_length=20, verbose_name='PAN No'),
        ),
    ]
