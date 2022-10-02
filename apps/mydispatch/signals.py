# from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import Group
# from http.client import HTTPResponse
from django.shortcuts import HttpResponse
# from django.db import transaction
from apps.accounts.models import User
from apps.mydispatch.models import Dispatch
from apps.profiles.models import Customer




@receiver(post_save, sender=Dispatch)
def create_user(sender, instance, created, **kwargs):
    if instance.customer_email:
        print((instance.customer_email).lower())
        party_name = instance.party_name
        print(party_name)
        if User.objects.filter(email=(instance.customer_email).lower()).exists():
            if Customer.objects.filter(business_name=str(instance)).exists():
                pass
            else:
                pass
        # elif Customer.objects.filter(business_name=str(instance)).exists():
        #     pass
        else:    
            if created:
                try:
                    cuser = User.objects.create(
                        email=(instance.customer_email).lower(), 
                        first_name=instance.customer_first_name, 
                        last_name=instance.customer_last_name, 
                        is_employee=False
                    )
                    cuser.is_customer=True
                    cuser.is_active=True
                    my_customer_group = Group.objects.get_or_create(name='CUSTOMERs')
                    my_customer_group[0].user_set.add(cuser)
                    cuser.save()
                    if cuser.is_customer:
                        cust = Customer.objects.create(user=cuser)
                        cust.business_name=str(instance)
                        cust.status = True
                        cust.save()
                        data = {"Role": "Customer"}
                except Exception as e:
                    return HttpResponse(e)



# @receiver(post_save, sender=Dispatch)
# def generate_dispatch_order_id(sender, instance, created, **kwargs):
#     if created:
#         date_format = instance.created_at.strftime("%Y%m%d%H%M%S")
#         if instance.party_name:
#             instance.dispatch_order_id = f"""{instance.party_name[0:2].upper()}{date_format}{10000+instance.pkid}"""
#         else:
#             instance.dispatch_order_id = f"""{instance.invoice_no.upper()}{date_format}{10000+instance.pkid}"""
#         instance.save()
