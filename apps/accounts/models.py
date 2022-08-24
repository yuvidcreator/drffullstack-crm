import datetime
import uuid

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator

from apps.accounts.managers import CustomUserManager

# Create your models here.


class User(AbstractBaseUser, PermissionsMixin):
    pkid = models.BigAutoField(primary_key=True, editable=False)
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    username = None
    email = models.EmailField(verbose_name=_("Email Address"), unique=True)
    mobile_regex = RegexValidator(
        regex=r'^\+?91?\d{9,12}$', 
        message="Phone number must be entered in the format: '+919999999999'. Up to 10 digits allowed."
    )
    mobile = models.CharField(
        validators=[mobile_regex],
        max_length=13,
        verbose_name=_("Mobile No"),
        unique=True,
        null=True,
        blank=True,
    )
    full_name = models.CharField(max_length=50, blank=True, verbose_name=_("Full Name"))
    first_name = models.CharField(
        max_length=64, blank=True, verbose_name=_("First Name")
    )
    last_name = models.CharField(max_length=64, blank=True, verbose_name=_("Last Name"))
    date_joined = models.DateTimeField(
        default=timezone.now, verbose_name=_("Registered On")
    )
    updated_date = models.DateTimeField(
        auto_now=True, verbose_name=_("Last Updated On")
    )

    # User Level flags
    is_blocked = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    is_mainadmin = models.BooleanField(default=False, verbose_name=_("Is Admin"))
    is_manager = models.BooleanField(default=False, verbose_name=_("Is Manager"))
    is_accountant = models.BooleanField(default=False, verbose_name=_("Is Accountant"))
    is_salesman = models.BooleanField(default=False, verbose_name=_("Is Salesman"))
    is_customer = models.BooleanField(default=False, verbose_name=_("Is Customer"))

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = [
        "mobile",
        "first_name",
        "last_name",
        "is_mainadmin",
        "is_manager",
        "is_accountant",
        "is_salesman",
        "is_customer",
    ]

    objects = CustomUserManager()

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")
        db_table = "users"  # Table Name

    @property
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def _str_(self):
        return f"{self.full_name}"
