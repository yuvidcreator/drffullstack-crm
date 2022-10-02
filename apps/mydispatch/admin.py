from django.contrib import admin
# from django.contrib.auth.models import Group, Permission
# from django.urls import reverse
# from django.utils.safestring import mark_safe

from apps.mydispatch.models import Dispatch, DispatchRecievedReciepts

# Register your models here.



class TabularInlineBase(admin.TabularInline):
    list_per_page = 2



class DispatchRecieptsInline(TabularInlineBase):
    model = DispatchRecievedReciepts



@admin.register(Dispatch)
class DispatchAdmin(admin.ModelAdmin):
    search_fields = ["invoice_no","party_name",]
    readonly_fields= []
    list_display = [
        "pkid",
        "dispatch_order_id",
        "invoice_no",
        "party_name",
        "product",
        "salesman",
        "pick_list",
        "bill_status",
        "delivered_man",
        "delivery_date",
        "picker_name",
        "dispatch_status",
        "recieved_status",
    ]
    list_display_links = list_display
    exclude = []
    inlines = [DispatchRecieptsInline]