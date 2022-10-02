from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from .models import User


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = User
        fields = [
            "email",
            "first_name",
            "last_name",
            "is_employee",
            "is_customer",
        ]
        error_class = "error"


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = [
            "email",
            "first_name",
            "last_name",
            "is_employee",
            "is_customer",
        ]
        error_class = "error"
