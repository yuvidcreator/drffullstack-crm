from django.urls import path

from .views import (CustomerListAPIView, GetEmployeAPIView, UpdateEmployeeAPIView)

urlpatterns = [
    path("employee/", GetEmployeAPIView.as_view(), name="get_employee_profile"),
    path(
        "update/<int:pkid>/", UpdateEmployeeAPIView.as_view(), name="update_employee_profile"
    ),
    path("customers/", CustomerListAPIView.as_view(), name="get_all_customers"),
]
