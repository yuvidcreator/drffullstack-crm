from django.urls import path

from .views import CustomerListAPIView, GetProfileAPIView, UpdateProfileAPIView

urlpatterns = [
    path("me/", GetProfileAPIView.as_view(), name="get_user_profile"),
    path(
        "update/<int:pkid>/", UpdateProfileAPIView.as_view(), name="update_user_profile"
    ),
    path("customers/", CustomerListAPIView.as_view(), name="get_all_customers"),
]
