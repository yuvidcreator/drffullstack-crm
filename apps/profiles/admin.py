from django.contrib import admin
from .models import *

# Register your models here.


class ProfileAdmin(admin.ModelAdmin):
    list_display=["pkid", "id", "user", "gender", "is_employee", "city", "zip_code"]
    list_filter=["gender","city","zip_code","state"]
    list_display_links=["pkid", "id", "user"]



admin.site.register(Profile, ProfileAdmin)


class CustomerAdmin(admin.ModelAdmin):
    list_display=["pkid", "id", "user", "gender", "city", "zip_code"]
    list_filter=["gender","city","zip_code","state"]
    list_display_links=["pkid", "id", "user"]



admin.site.register(Customer, CustomerAdmin)