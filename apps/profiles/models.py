import datetime
from email.policy import default
import uuid
from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone
from django.utils.crypto import get_random_string
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator

from apps.common.models import TimeStampUUIDModel
from djCRMBackend.dependancies import path_and_rename

# Create your models here.


User = get_user_model()


def employee_kyc_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
        return 'employees/kyc/user_{0}/{1}'.format(instance.user.pkid, filename)


def customer_kyc_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
        return 'customers/kyc/user_{0}/{1}'.format(instance.user.pkid, filename)


class Gender(models.TextChoices):
    MALE = "Male", _("Male")
    FEMALE = "Female", _("Female")
    OTHER = "Other", _("Other")
    SELECT = "Select", _("Select")


# Profiles Model
class Employee(TimeStampUUIDModel):
    user = models.OneToOneField(User, related_name="employee_profiles", on_delete=models.CASCADE)
    emp_id = models.CharField(max_length=50, blank=True, verbose_name=_("Employee ID"))
    profile_picture = models.ImageField(
        default="default.jpg",
        upload_to=employee_kyc_path,
        blank=True,
        verbose_name=_("Employee's Image"),
    )
    date_of_birth = models.DateField(
        blank=True, null=True, verbose_name=_("Date of Birth")
    )
    gender = models.CharField(
        max_length=20,
        verbose_name=_("Gender"),
        choices=Gender.choices,
        default=Gender.SELECT,
        blank=True,
    )
    address_line1 = models.CharField(
        max_length=255, blank=True, verbose_name=_("Address Line 1")
    )
    address_line2 = models.CharField(
        max_length=255, blank=True, verbose_name=_("Address Line 2")
    )
    city = models.CharField(max_length=255, blank=True, verbose_name=_("City"))
    zip_code = models.CharField(max_length=10, blank=True, verbose_name=_("Zip Code"))
    state = models.CharField(max_length=255, blank=True, verbose_name=_("State"))
    country = models.CharField(
        max_length=255, blank=True, verbose_name=_("Country"), default="India"
    )
    about_me = models.TextField(blank=True, verbose_name=_("About Employee"))
    eduaction = models.CharField(
        max_length=255, blank=True, verbose_name=_("Educational Qualification")
    )
    work_experience = models.CharField(
        max_length=255, blank=True, verbose_name=_("Work Experience")
    )
    adhaar_no = models.PositiveBigIntegerField(
        default=000000000000, blank=True, verbose_name=_("Adhaar No")
    )
    adhaar_certificate1 = models.FileField(
        upload_to=employee_kyc_path, blank=True, verbose_name=_("Adhaar Certificate Front")
    )
    adhaar_certificate2 = models.FileField(
        upload_to=employee_kyc_path, blank=True, verbose_name=_("Adhaar Certificate Back")
    )
    pan_no = models.CharField(
        max_length=20, blank=True, verbose_name=_("PAN No")
    )
    pan_certificate = models.FileField(
        upload_to=employee_kyc_path, blank=True, verbose_name=_("Upload PAN")
    )
    bank_details = models.CharField(
        max_length=255, blank=True, verbose_name=_("Bank Details")
    )
    salary = models.IntegerField(default=0, blank=True, verbose_name=_("Salary"))
    is_mobile_verified = models.BooleanField(
        default=False, verbose_name=_("Mobile verified")
    )
    status = models.BooleanField(default=False, verbose_name=_("Employee Status"))

    is_admin = models.BooleanField(
        default=False, verbose_name=_("Is Admin")
    )
    is_manager = models.BooleanField(
        default=False, verbose_name=_("Is Manager")
    )
    is_accountant = models.BooleanField(
        default=False, verbose_name=_("Is Accountant")
    )
    is_salesman = models.BooleanField(
        default=False, verbose_name=_("Is Salesman")
    )
    is_deliveryboy = models.BooleanField(
        default=False, verbose_name=_("Is Delivery Boy")
    )
    top_employee = models.BooleanField(
        default=False, verbose_name=_("Top Employee")
    )
    rating = models.DecimalField(
        max_digits=4, decimal_places=2, null=True, blank=True, verbose_name=_("Ratings")
    )
    num_reviews = models.IntegerField(
        verbose_name=_("Number of Reviews"), default=0, null=True, blank=True
    )

    def __str__(self):
        return f"{self.user.full_name}"


class Customer(TimeStampUUIDModel):
    user = models.OneToOneField(User, related_name="customer_profiles", on_delete=models.CASCADE)
    mobile_regex = RegexValidator(
        regex=r'^\d{9,10}$', 
        message="Phone number must be entered in the format: '9999999999'. Up to 10 digits allowed."
    )
    about_me = models.TextField(blank=True, null=True, verbose_name=_("About Customer"))
    profile_picture = models.ImageField(
        default="default.jpg",
        upload_to=customer_kyc_path,
        blank=True,
        verbose_name=_("Customer's Image"),
    )
    date_of_birth = models.DateField(
        blank=True, null=True, verbose_name=_("Date of Birth")
    )
    gender = models.CharField(
        max_length=20,
        verbose_name=_("Gender"),
        choices=Gender.choices,
        default=_("---"),
        blank=True,
    )
    address_line_1 = models.CharField(
        max_length=255, blank=True, null=True, verbose_name=_("Address Line 1")
    )
    address_line_2 = models.CharField(
        max_length=255, blank=True, null=True, verbose_name=_("Address Line 2")
    )
    city = models.CharField(
        max_length=255, blank=True, default=_("Pune"), verbose_name=_("City")
    )
    zip_code = models.CharField(
        max_length=10, blank=True, verbose_name=_("Zip Code")
    )
    state = models.CharField(
        max_length=255, blank=True, default=_("Maharashtra"), verbose_name=_("State")
    )
    country = models.CharField(
        max_length=255, blank=True, verbose_name=_("Country"), default=_("India")
    )

    # Business Related
    business_name = models.CharField(
        max_length=50, blank=True, null=True, verbose_name=_("Business Name")
    )
    business_wano = models.CharField(
        validators=[mobile_regex],
        max_length=10,
        verbose_name=_("Business WhatsApp No."),
        null=True,
        blank=True,
        default=0
    )
    business_address_line_1 = models.CharField(
        max_length=255, blank=True, verbose_name=_("Business Address Line 1")
    )
    business_address_line_2 = models.CharField(
        max_length=255, blank=True, verbose_name=_("Business Address Line 2")
    )
    business_area_name = models.CharField(
        max_length=64, blank=True, verbose_name=_("Area Name")
    )
    landmark = models.CharField(
        max_length=64, null=True, blank=True, verbose_name=_("Land Mark")
    )
    directions_to_reach = models.TextField(
        null=True, blank=True, verbose_name=_("Direction To Reach")
    )
    latitude = models.FloatField(
        default=19.214, blank=True, verbose_name=_("Set Latitude")
    )
    longitude = models.FloatField(
        default=19.214, blank=True, verbose_name=_("Set Longitude")
    )
    biz_googlemap_link = models.CharField(
        max_length=64, null=True, blank=True, verbose_name=_("Google Map Link")
    )
    business_zip_code = models.CharField(
        max_length=10, blank=True, verbose_name=_("Zip Code")
    )
    business_city = models.CharField(
        max_length=255, blank=True, verbose_name=_("City")
    )
    business_state = models.CharField(
        max_length=255, blank=True, verbose_name=_("State")
    )
    business_country = models.CharField(
        max_length=255, blank=True, verbose_name=_("Country"), default="India"
    )

    about_business = models.TextField(blank=True, verbose_name=_("About Business"))
    upi_id = models.CharField(max_length=50, blank=True, verbose_name=_("UPI ID"))
    adhaar_no = models.PositiveBigIntegerField(
        default=000000000000, blank=True, verbose_name=_("Adhaar No")
    )
    adhaar_certificate1 = models.FileField(
        upload_to=customer_kyc_path, blank=True, verbose_name=_("Adhaar Certificate Front")
    )
    adhaar_certificate2 = models.FileField(
        upload_to=customer_kyc_path, blank=True, verbose_name=_("Adhaar Certificate Back")
    )
    gst_no = models.CharField(
        max_length=20, blank=True, verbose_name=_("GST No")
    )
    gst_certificate = models.FileField(
        upload_to=customer_kyc_path, blank=True, verbose_name=_("Upload GST Doc.")
    )
    pan_no = models.CharField(max_length=20, blank=True, verbose_name=_("PAN No"))
    pan_certificate = models.FileField(
        upload_to=customer_kyc_path, blank=True, verbose_name=_("Upload PAN")
    )
    security_cheque = models.FileField(
        upload_to=customer_kyc_path, blank=True, verbose_name=_("Security Cheque")
    )
    visiting_card = models.FileField(
        upload_to=customer_kyc_path, blank=True, verbose_name=_("Visiting Card")
    )
    bank_details = models.CharField(
        max_length=255, blank=True, verbose_name=_("Bank Details")
    )
    is_mobile_verified = models.BooleanField(
        default=False, verbose_name=_("Mobile verified")
    )
    is_verified_customer = models.BooleanField(
        default=False, verbose_name=_("Customer verified")
    )
    status = models.BooleanField(default=False, verbose_name=_("Customer Status"))
    top_customer = models.BooleanField(default=False, verbose_name=_("Top Customer"))
    rating = models.DecimalField(
        max_digits=4, decimal_places=2, null=True, blank=True, verbose_name=_("Ratings")
    )
    num_reviews = models.IntegerField(
        verbose_name=_("Number of Reviews"), default=0, null=True, blank=True
    )

    def __str__(self):
        return f"{self.user.full_name}"
