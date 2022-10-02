import datetime
from django.utils import timezone
import uuid
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.common.models import TimeStampUUIDModel

# Create your models here.



class ProductTypes(models.TextChoices):
    HERO = "Hero", _("Hero")
    BATTERY = "Battery", _("Battery")
    TYRE = "Tyre", _("Tyre")




class Product(models.Model):
    pkid = models.BigAutoField(primary_key=True, editable=False)
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=120, blank=True, verbose_name=_("Product Name"))
    part_no = models.CharField(max_length=120, blank=True, verbose_name=_("Part No"))
    brand = models.CharField(max_length=120, blank=True, verbose_name=_("Brand"))
    type_of_product = models.CharField(
        max_length=255, 
        choices=ProductTypes.choices, 
        default=_("Select Product Type"), 
        verbose_name=_("Product Type")
    )
    capacity = models.CharField(
        max_length=5, 
        blank=True, 
        default=0.0, 
        verbose_name=_("Battery Capacity"), 
        help_text=_("If Product is Battery Please fill Capacity, otherwise Leave Blank")
    )
    description = models.TextField(blank=True, null=True, verbose_name=_("Product Description"))
    sku = models.CharField(
        max_length=255, 
        blank=True, 
        unique=True,
        verbose_name=_("Product SKU"), 
        help_text=_("This is a Stock Keeping Unit, which is a Unique No.")
    )
    main_image = models.ImageField(
        default="default.jpg",
        upload_to="products_images/{product.typeOfProduct}",
        blank=True,
        verbose_name=_("Hero Image"),
    )
    price = models.PositiveBigIntegerField(default=0, verbose_name=_("Price"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Created At"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Updated At"))

    class Meta:
        verbose_name=_("Product")
        verbose_name_plural=_("Products")
        db_table = "products"  # Table Name

    def __str__(self):
        return self.name




class ProductImages(TimeStampUUIDModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name=_("Select Product Name"))
    image = models.ImageField(
        upload_to="products_images/{product.typeOfProduct}", 
        blank=True, 
        verbose_name=_("Set Image (1920 x 1280px)"), 
        help_text=_("Image size should be 1920 x 1280px")
    )




# class HB(TimeStampUUIDModel):
#     product = models.ManyToManyField(Product, related_name="product_hb", verbose_name=_("HB"))

#     class Meta:
#         verbose_name=_("Hero Battery")
#         verbose_name_plural=_("HBs")
#         db_table = "hbs"  # Table Na

#     def __str__(self):
#         return f"{self.hero} + {self.battery}"


# class HT(TimeStampUUIDModel):
#     product = models.ManyToManyField(Product, related_name="product_ht", verbose_name=_("HT"))

#     class Meta:
#         verbose_name=_("Hero Tyre")
#         verbose_name_plural=_("HTs")
#         db_table = "hts"  # Table Na

#     def __str__(self):
#         return f"{self.hero} + {self.tyre}"


# class Hero(TimeStampUUIDModel):
#     name = models.CharField(max_length=50, default=_("Hero"), verbose_name=_("Product Type"))
#     product = models.ForeignKey(Product, related_name="hero_product", blank=True, null=True, verbose_name=_("Select Hero Product"))

#     class Meta:
#         verbose_name=_("Hero Product")
#         verbose_name_plural=_("Hero Products")
#         db_table = "hero_products"  # Table Na

#     def __str__(self):
#         return f"{self.name}"


# class Battery(TimeStampUUIDModel):
#     name = models.CharField(max_length=50, default=_("Battery"), verbose_name=_("Product Type"))
#     product = models.ForeignKey(Product, related_name="battery_product", blank=True, null=True, verbose_name=_("Select Battery"))

#     class Meta:
#         verbose_name=_("Battery Product")
#         verbose_name_plural=_("Battery Products")
#         db_table = "battery_products"  # Table Na

#     def __str__(self):
#         return f"{self.name}"


# class Tyre(TimeStampUUIDModel):
#     name = models.CharField(max_length=50, default=_("Tyre"), verbose_name=_("Product Type"))
#     product = models.ForeignKey(Product, related_name="tyre_product", blank=True, null=True, verbose_name=_("Select Tyre"))

#     class Meta:
#         verbose_name=_("Tyre Product")
#         verbose_name_plural=_("Tyre Products")
#         db_table = "tyre_products"  # Table Na

#     def __str__(self):
#         return f"{self.name}"