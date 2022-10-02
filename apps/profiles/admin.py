from django.contrib import admin

from .models import Employee, Customer

# Register your models here.


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ["pkid", "id", "user", "gender", "is_admin", "is_manager", "is_accountant", "is_salesman", "is_deliveryboy"]
    list_filter = ["gender", "city", "zip_code", "state"]
    list_display_links = ["pkid", "id", "user"]


admin.site.register(Employee, EmployeeAdmin)


class CustomerAdmin(admin.ModelAdmin):
    list_display = ["pkid", "id", "user", "gender", "business_name", "business_wano", "city", "zip_code"]
    list_filter = ["gender", "city", "zip_code", "state"]
    list_display_links = ["pkid", "id", "user"]


admin.site.register(Customer, CustomerAdmin)
