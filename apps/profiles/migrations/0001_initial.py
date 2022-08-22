# Generated by Django 3.2.9 on 2022-08-21 20:38

import djCRMBackend.dependancies
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('pkid', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('emp_id', models.CharField(blank=True, max_length=50, verbose_name='Employee ID')),
                ('profile_picture', models.ImageField(blank=True, default='default.jpg', upload_to='profiles/profile_pics', verbose_name='Profile Image')),
                ('date_of_birth', models.DateField(blank=True, null=True, verbose_name='Date of Birth')),
                ('gender', models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other'), ('Select', 'Select')], default='Select', max_length=20, verbose_name='Gender')),
                ('address_line_1', models.CharField(blank=True, max_length=255, verbose_name='Address Line 1')),
                ('address_line_2', models.CharField(blank=True, max_length=255, verbose_name='Address Line 2')),
                ('city', models.CharField(blank=True, max_length=255, verbose_name='City')),
                ('zip_code', models.CharField(blank=True, max_length=10, verbose_name='Zip Code')),
                ('state', models.CharField(blank=True, max_length=255, verbose_name='State')),
                ('country', models.CharField(blank=True, default='India', max_length=255, verbose_name='Country')),
                ('about_me', models.TextField(blank=True, verbose_name='About Me')),
                ('eduaction', models.CharField(blank=True, max_length=255, verbose_name='Educational Qual.')),
                ('work_experience', models.CharField(blank=True, max_length=255, verbose_name='Work Experience')),
                ('pan_no', models.CharField(blank=True, max_length=20, verbose_name='PAN No')),
                ('bank_details', models.CharField(blank=True, max_length=255, verbose_name='Bank Details')),
                ('salary', models.IntegerField(blank=True, default=0, verbose_name='Salary')),
                ('is_mobile_verified', models.BooleanField(default=False, verbose_name='Mobile verified')),
                ('status', models.BooleanField(default=False, verbose_name='Profile Status')),
                ('is_employee', models.BooleanField(default=False, verbose_name='Is Employee')),
                ('is_deliveryboy', models.BooleanField(default=False, verbose_name='Is Delivery Boy')),
                ('top_employee', models.BooleanField(default=False, verbose_name='Top Employee')),
                ('check_in', models.TimeField(blank=True, null=True, verbose_name='Check In')),
                ('check_out', models.TimeField(blank=True, null=True, verbose_name='Check Out')),
                ('rating', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True, verbose_name='Ratings')),
                ('num_reviews', models.IntegerField(blank=True, default=0, null=True, verbose_name='Number of Reviews')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profiles', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('pkid', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('about_me', models.TextField(blank=True, verbose_name='About Me')),
                ('profile_picture', models.ImageField(blank=True, default='default.jpg', upload_to='customers/profile_pics', verbose_name='Profile Image')),
                ('date_of_birth', models.DateField(blank=True, null=True, verbose_name='Date of Birth')),
                ('gender', models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other'), ('Select', 'Select')], default='--', max_length=20, verbose_name='Gender')),
                ('address_line_1', models.CharField(blank=True, max_length=255, verbose_name='Address Line 1')),
                ('address_line_2', models.CharField(blank=True, max_length=255, verbose_name='Address Line 2')),
                ('business_name', models.CharField(blank=True, max_length=50, verbose_name='Business Name')),
                ('business_wano', models.IntegerField(blank=True, default=910000000000, verbose_name='Business WhatsApp No.')),
                ('biz_address_line_1', models.CharField(blank=True, max_length=255, verbose_name='Business Address Line 1')),
                ('biz_address_line_2', models.CharField(blank=True, max_length=255, verbose_name='Business Address Line 2')),
                ('area_name', models.CharField(blank=True, max_length=64, verbose_name='Area Name')),
                ('landmark', models.CharField(blank=True, max_length=64, null=True, verbose_name='Land Mark')),
                ('directions_to_reach', models.TextField(blank=True, null=True, verbose_name='Direction To Reach')),
                ('latitude', models.FloatField(blank=True, default=19.214, verbose_name='Latitude')),
                ('longitude', models.FloatField(blank=True, default=19.214, verbose_name='Longitude')),
                ('google_map_link', models.CharField(blank=True, max_length=64, null=True, verbose_name='Google Map Link')),
                ('zip_code', models.CharField(blank=True, max_length=10, verbose_name='Zip Code')),
                ('city', models.CharField(blank=True, max_length=255, verbose_name='City')),
                ('state', models.CharField(blank=True, max_length=255, verbose_name='State')),
                ('country', models.CharField(blank=True, default='India', max_length=255, verbose_name='Country')),
                ('about_business', models.TextField(blank=True, verbose_name='About Business')),
                ('gst_no', models.CharField(blank=True, max_length=20, verbose_name='GST No')),
                ('upload_gst', models.FileField(blank=True, upload_to=djCRMBackend.dependancies.path_and_rename, verbose_name='Upload GST Doc.')),
                ('pan_no', models.CharField(blank=True, max_length=20, verbose_name='PAN No')),
                ('upload_pan', models.FileField(blank=True, upload_to=djCRMBackend.dependancies.path_and_rename, verbose_name='Upload PAN')),
                ('bank_details', models.CharField(blank=True, max_length=255, verbose_name='Bank Details')),
                ('is_mobile_verified', models.BooleanField(default=False, verbose_name='Mobile verified')),
                ('is_verified_customer', models.BooleanField(default=False, verbose_name='Customer verified')),
                ('status', models.BooleanField(default=False, verbose_name='Customer Status')),
                ('top_customer', models.BooleanField(default=False, verbose_name='Top Customer')),
                ('rating', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True, verbose_name='Ratings')),
                ('num_reviews', models.IntegerField(blank=True, default=0, null=True, verbose_name='Number of Reviews')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customers', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
