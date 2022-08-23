from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.profiles.models import Customer, Profile
from djCRMBackend.settings.base import AUTH_USER_MODEL


@receiver(post_save, sender=AUTH_USER_MODEL)
def create_user(sender, instance, created, **kwargs):
    if instance.is_mainadmin:
        if created:
            instance.is_mainadmin = True
            data = {"role": "Admin"}
            if instance.email:
                pro = Profile.objects.create(user=instance)
                pro.is_employee = True
                pro.status = True
                pro.save()
    elif instance.is_manager:
        if created:
            instance.is_manager = True
            data = {"Role": "Manager"}
            if instance.email:
                pro = Profile.objects.create(user=instance)
                pro.is_employee = True
                pro.status = True
                pro.save()
    elif instance.is_accountant:
        if created:
            instance.is_accountant = True
            data = {"Role": "Accountant"}
            if instance.email:
                pro = Profile.objects.create(user=instance)
                pro.is_employee = True
                pro.status = True
                pro.save()
    elif instance.is_salesman:
        if created:
            instance.is_salesman = True
            data = {"Role": "Salesman"}
            if instance.email:
                pro = Profile.objects.create(user=instance)
                pro.is_employee = True
                pro.is_deliveryboy = True
                pro.status = True
                pro.save()
    elif instance.is_customer:
        if created:
            instance.is_customer = True
            data = {"Role": "Customer"}
            if instance.email:
                cust = Customer.objects.create(user=instance)
                cust.status = True
                cust.save()
    else:
        if created:
            data = {"Role": "Employee"}
            if instance.email:
                pro = Profile.objects.create(user=instance)
                pro.is_employee = True
                pro.status = True
                pro.save()
