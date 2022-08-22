import datetime
from unittest.mock import DEFAULT
from django.contrib.auth import get_user_model
from django.utils import timezone
import uuid
from django.utils.crypto import get_random_string
from django.conf import settings
from django.db import models
from apps.common.models import TimeStampUUIDModel
from django.utils.translation import gettext_lazy as _
from djCRMBackend.dependancies import path_and_rename

# Create your models here.


User = get_user_model()

class Gender(models.TextChoices):
    MALE = "Male", _("Male")
    FEMALE = "Female", _("Female")
    OTHER = "Other", _("Other")
    SELECT = "Select", _("Select")


# Profiles Model
class Profile(TimeStampUUIDModel):
    user = models.ForeignKey(User, related_name="profiles", on_delete=models.CASCADE)
    emp_id = models.CharField(max_length=50, blank=True, verbose_name=_("Employee ID"))
    profile_picture = models.ImageField(
        default="default.jpg", upload_to="profiles/profile_pics", blank=True, verbose_name=_("Profile Image")
    )
    date_of_birth = models.DateField(blank=True, null=True, verbose_name=_("Date of Birth"))
    gender = models.CharField(max_length=20, verbose_name=_("Gender"), choices=Gender.choices, default=Gender.SELECT, blank=True)
    address_line_1 = models.CharField(max_length=255, blank=True, verbose_name=_("Address Line 1"))
    address_line_2 = models.CharField(max_length=255, blank=True, verbose_name=_("Address Line 2"))
    city = models.CharField(max_length=255, blank=True, verbose_name=_("City"))
    zip_code = models.CharField(max_length=10, blank=True, verbose_name=_("Zip Code"))
    state = models.CharField(max_length=255, blank=True, verbose_name=_("State"))
    country = models.CharField(max_length=255, blank=True, verbose_name=_("Country"), default="India")
    about_me = models.TextField(blank=True, verbose_name=_("About Me"))
    eduaction = models.CharField(max_length=255, blank=True, verbose_name=_("Educational Qual."))
    work_experience = models.CharField(max_length=255, blank=True, verbose_name=_("Work Experience"))
    pan_no = models.CharField(max_length=20, blank=True, verbose_name=_("PAN No"))
    bank_details = models.CharField(max_length=255, blank=True, verbose_name=_("Bank Details"))
    salary = models.IntegerField(default=0, blank=True, verbose_name=_("Salary"))
    is_mobile_verified = models.BooleanField(default=False, verbose_name=_("Mobile verified"))
    status = models.BooleanField(default=False, verbose_name=_("Profile Status"))
    is_employee = models.BooleanField(default=False, verbose_name=_("Is Employee"))
    is_deliveryboy = models.BooleanField(default=False, verbose_name=_("Is Delivery Boy"))
    top_employee = models.BooleanField(default=False, verbose_name=_("Top Employee"))
    check_in = models.TimeField(verbose_name=_("Check In"), blank=True, null=True)
    check_out = models.TimeField(verbose_name=_("Check Out"), blank=True, null=True)
    rating = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True, verbose_name=_("Ratings"))
    num_reviews = models.IntegerField(
        verbose_name=_("Number of Reviews"), default=0, null=True, blank=True
    )


    def __str__(self):
        return f"{self.user.full_name}"



class Customer(TimeStampUUIDModel):
    user = models.ForeignKey(User, related_name="customers", on_delete=models.CASCADE)
    about_me = models.TextField(blank=True, verbose_name=_("About Me"))
    profile_picture = models.ImageField(
        default="default.jpg", upload_to="customers/profile_pics", blank=True, verbose_name=_("Profile Image")
    )
    date_of_birth = models.DateField(blank=True, null=True, verbose_name=_("Date of Birth"))
    gender = models.CharField(max_length=20, verbose_name=_("Gender"), choices=Gender.choices, default="--", blank=True)
    address_line_1 = models.CharField(max_length=255, blank=True, verbose_name=_("Address Line 1"))
    address_line_2 = models.CharField(max_length=255, blank=True, verbose_name=_("Address Line 2"))
    city = models.CharField(max_length=255, blank=True, verbose_name=_("City"))
    zip_code = models.CharField(max_length=10, blank=True, verbose_name=_("Zip Code"))
    state = models.CharField(max_length=255, blank=True, verbose_name=_("State"))
    country = models.CharField(max_length=255, blank=True, verbose_name=_("Country"), default="India")

    #Business Related
    business_name = models.CharField(max_length=50, blank=True, verbose_name=_("Business Name"))
    business_wano = models.IntegerField(default=910000000000, blank=True, verbose_name=_("Business WhatsApp No."))
    biz_address_line_1 = models.CharField(max_length=255, blank=True, verbose_name=_("Business Address Line 1"))
    biz_address_line_2 = models.CharField(max_length=255, blank=True, verbose_name=_("Business Address Line 2"))
    area_name = models.CharField(max_length=64, blank=True, verbose_name=_("Area Name"))
    landmark = models.CharField(max_length=64, null=True, blank=True, verbose_name=_("Land Mark"))
    directions_to_reach = models.TextField(null=True, blank=True, verbose_name=_("Direction To Reach"))
    latitude = models.FloatField(default=19.214, blank=True, verbose_name=_("Latitude"))
    longitude = models.FloatField(default=19.214, blank=True, verbose_name=_("Longitude"))
    google_map_link = models.CharField(max_length=64, null=True, blank=True, verbose_name=_("Google Map Link"))
    zip_code = models.CharField(max_length=10, blank=True, verbose_name=_("Zip Code"))
    city = models.CharField(max_length=255, blank=True, verbose_name=_("City"))
    state = models.CharField(max_length=255, blank=True, verbose_name=_("State"))
    country = models.CharField(max_length=255, blank=True, verbose_name=_("Country"), default="India")

    about_business = models.TextField(blank=True, verbose_name=_("About Business"))
    gst_no = models.CharField(max_length=20, blank=True, verbose_name=_("GST No"))
    upload_gst = models.FileField(upload_to=path_and_rename, blank=True, verbose_name=_("Upload GST Doc."))
    pan_no = models.CharField(max_length=20, blank=True, verbose_name=_("PAN No"))
    upload_pan = models.FileField(upload_to=path_and_rename, blank=True, verbose_name=_("Upload PAN"))
    bank_details = models.CharField(max_length=255, blank=True, verbose_name=_("Bank Details"))
    is_mobile_verified = models.BooleanField(default=False, verbose_name=_("Mobile verified"))
    is_verified_customer = models.BooleanField(default=False, verbose_name=_("Customer verified"))
    status = models.BooleanField(default=False, verbose_name=_("Customer Status"))
    top_customer = models.BooleanField(default=False, verbose_name=_("Top Customer"))
    rating = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True, verbose_name=_("Ratings"))
    num_reviews = models.IntegerField(
        verbose_name=_("Number of Reviews"), default=0, null=True, blank=True
    )

    def __str__(self):
        return f"{self.user.full_name}"
