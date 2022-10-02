# import datetime
import uuid
from django.core.validators import RegexValidator
# from django.db.models.signals import post_save
from django.dispatch import receiver
# from django.contrib.auth.models import Group
from django.db import models
# from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from apps.common.models import TimeStampUUIDModel
# from apps.accounts.models import User
from apps.profiles.models import Employee
# from apps.products.models import Product

# Create your models here.




class ProductTypes(models.TextChoices):
    H = "Hero", _("Hero")
    B = "Battery", _("Battery")
    T = "Tyre", _("Tyre")
    HB = "Hero + Battery", _("Hero + Battery")
    BT = "Battery + Tyre", _("Battery + Tyre")
    HT = "Hero + Tyre", _("Hero + Tyre")
    HBT = "Hero + Battery + Tyre", _("Hero + Battery + Tyre")
    



class BillStatus(models.TextChoices):
    INCOMPLETE = "Incomplete", _("Incomplete")
    COMPLETE = "Complete", _("Complete")



class DispchStatus(models.TextChoices):
    PENDING = "Pending", _("Pending")
    COMPLETED = "Completed", _("Completed")
    HOLD = "Hold", _("Hold")
    CANCEL = "Cancel", _("Cancel")


class RecievedStatus(models.TextChoices):
    INCOMPLETE = "Incomplete", _("Incomplete")
    COMPLETE = "Complete", _("Complete")


class PaymentMethod(models.TextChoices):
    PNR = "Payment Not Recived", _("Payment Not Recived")
    COD = "Cash On Delivery", _("Cash On Delivery")
    ONLINE = "Online Mode", _("Online Mode")
    CHEQUE = "Cheque", _("Cheque")
    OTHER = "Other", _("Other")


class RatingChoices(models.TextChoices):
    GOOD = "Good", _("Good")
    AVERAGE = "Average", _("Average")
    POOR = "Poor", _("Poor")
    BAD = "BAD", _("BAD")



def dispatch_fileuploads_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
        return 'dispatch/%Y/%m/%d/{instance.party_name}/'.format(instance.party_name, filename)

class Dispatch(models.Model):
    pkid = models.BigAutoField(primary_key=True, editable=False)
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    dispatch_order_id = models.CharField(max_length=50, editable=False)
    invoice_no = models.CharField(
        max_length=50, verbose_name=_("Invoice / Bill No"), blank=True, null=True, unique=True
    )
    party_name = models.CharField(
        max_length=255, verbose_name=_("Party / Business Name")
    )
    customer_first_name = models.CharField(
        max_length=100, verbose_name=_("Customer First Name"), blank=True
    )
    customer_last_name = models.CharField(
        max_length=100, verbose_name=_("Customer Last Name"), blank=True
    )
    mobile_regex = RegexValidator(
        regex=r'^\d{9,10}$', 
        message=_("Phone number must be entered in the format: '9999999999'. Up to 10 digits allowed.")
    )
    customer_mobile = models.CharField(
        validators=[mobile_regex],
        max_length=10,
        verbose_name=_("Mobile No"),
        blank=True,
        null=True
    )
    customer_email = models.EmailField(
        verbose_name=_("Email Address"), blank=True, null=True, unique=True
    )
    hs_code = models.CharField(
        max_length=50, verbose_name=_("HS Code"), blank=True, null=True, unique=True
    )
    rc_code = models.CharField(
        max_length=50, verbose_name=_("RC Code"), blank=True, null=True, unique=True
    )
    # product = models.ManyToManyField()
    product = models.CharField(
        max_length=50, 
        choices=ProductTypes.choices, 
        default=_("Select Product(s)"), 
        verbose_name=_("Select Product(s) Type")
    )
    total_price = models.PositiveBigIntegerField(
        blank=True, default=0, verbose_name=_("Product Price")
    )
    salesman = models.ForeignKey(
        Employee, 
        on_delete=models.PROTECT, 
        related_name="employee_salesman", 
        verbose_name=_("Salesman Name")
    )
    pick_list = models.PositiveIntegerField(
        default=0, blank=True, verbose_name=_("Pick List")
    )
    bill_status = models.CharField(
        max_length=255, 
        verbose_name=_("Bill Status"), 
        choices=BillStatus.choices, 
        default=_("Select")
    )
    delivered_man = models.ForeignKey(
        Employee, 
        on_delete=models.PROTECT, 
        blank=True, 
        related_name="delivered_by", 
        verbose_name=_("Delivered By")
    )
    delivery_date = models.DateTimeField(
        auto_now=False, 
        auto_now_add=False, 
        verbose_name=_("Enter Delivery Date")
    )
    picker_name = models.ForeignKey(
        Employee, 
        on_delete=models.PROTECT, 
        related_name="picker_name", 
        verbose_name=_("Picker Name")
    )
    dispatch_status = models.CharField(
        max_length=120, 
        verbose_name=_("Dispatch Status"), 
        choices=DispchStatus.choices, 
        default=_("Select Status"), 
        blank=True
    )
    recieved_status = models.CharField(
        max_length=120, 
        verbose_name=_("Recieved Status"), 
        choices=RecievedStatus.choices, 
        default=_("Select Status"), 
        blank=True
    )
    # recieved_reciepts = models.FileField(
    #     upload_to="dispatch/", 
    #     blank=True, 
    #     verbose_name=_("Upload Recieved Reciept")
    # )
    payment_method = models.CharField(
        max_length=100, 
        blank=True, 
        null=True, 
        choices=PaymentMethod.choices, 
        default="Select Payment Method", 
        verbose_name=_("Payment Mode")
    )
    remark = models.CharField(
        max_length=255, verbose_name=_("Remark"), blank=True
    )
    refunded_amount = models.FloatField(default=0, verbose_name=_("Refunded Amount"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Date Time"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Updated At"))
    check_in = models.DateField()
    check_out = models.DateField()

    # Order Cancel Request
    is_cancel_requested = models.BooleanField(default=False)
    cancel_request_date = models.DateTimeField(blank=True, null=True)
    cancel_reason = models.CharField(max_length=255, blank=True, null=True)
    cancel_reason_details = models.TextField(blank=True, null=True)
    cancel_request_status = models.CharField(max_length=255, blank=True, null=True)


    class Meta:
        ordering = ["-created_at"]
        verbose_name=_("Dispatch")
        verbose_name_plural=_("Dispatches")
        db_table = "dispatches"  # Table Na

    def __str__(self):
        return f"{self.party_name}"



class DispatchRecievedReciepts(TimeStampUUIDModel):
    dispatch = models.ForeignKey(
        Dispatch, on_delete=models.CASCADE, related_name="recieved_reciepts"
    )
    reciepts = models.FileField(upload_to=dispatch_fileuploads_path, blank=True, null=True)

    class Meta:
        verbose_name = _("Dispatch Recieved Reciept")
        verbose_name_plural = _("Dispatch Recieved Reciepts")
        db_table = "dispatch_recieved_reciepts"

    def __str__(self):
        return self.reciepts.url
