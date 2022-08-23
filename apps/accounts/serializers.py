from django.db import IntegrityError, transaction
from djoser.conf import settings
from djoser.serializers import UserCreateSerializer
from rest_framework import serializers
from rest_framework.response import Response

from apps.accounts.models import User
from apps.profiles.models import Profile


class UserSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(source="get_full_name")

    class Meta:
        model = User
        fields = [
            "id",
            "pkid",
            "first_name",
            "last_name",
            "full_name",
            "email",
            "mobile",
            "is_staff",
            "is_active",
            "is_superuser",
            "is_mainadmin",
            "is_manager",
            "is_accountant",
            "is_salesman",
            "is_customer",
        ]

    def get_first_name(self, obj):
        return obj.first_name.title()

    def get_last_name(self, obj):
        return obj.last_name.title()

    def get_email(self, obj):
        return obj.email

    def get_mobile(self, obj):
        return obj.mobile

    def to_representation(self, instance):
        represenatation = super(UserSerializer, self).to_representation(instance)
        if instance.is_superuser:
            represenatation["is_superuser"] = True
        if instance.is_mainadmin:
            represenatation["is_mainadmin"] = True
        if instance.is_manager:
            represenatation["is_manager"] = True
        if instance.is_accountant:
            represenatation["is_accountant"] = True
        if instance.is_salesman:
            represenatation["is_salesman"] = True
        if instance.is_customer:
            represenatation["is_customer"] = True
        return represenatation


class TokenSerializer(serializers.ModelSerializer):
    auth_token = serializers.CharField(source="key")
    is_staff = serializers.BooleanField(source="user.is_staff")
    is_mainadmin = serializers.BooleanField(source="user.is_mainadmin")
    is_manager = serializers.BooleanField(source="user.is_manager")
    is_accountant = serializers.BooleanField(source="user.is_accountant")
    is_salesman = serializers.BooleanField(source="user.is_salesman")
    is_customer = serializers.BooleanField(source="user.is_customer")

    class Meta:
        model = settings.TOKEN_MODEL
        fields = (
            "auth_token",
            "is_staff",
            "is_mainadmin",
            "is_manager",
            "is_accountant",
            "is_salesman",
            "is_customer",
        )


class CreateUserSerializer(UserCreateSerializer):
    is_employee = serializers.BooleanField()
    is_mainadmin = serializers.BooleanField()
    is_manager = serializers.BooleanField()
    is_accountant = serializers.BooleanField()
    is_salesman = serializers.BooleanField()
    is_customer = serializers.BooleanField()

    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = [
            "id",
            "pkid",
            "first_name",
            "last_name",
            "email",
            "mobile",
            "is_mainadmin",
            "is_manager",
            "is_accountant",
            "is_salesman",
            "is_customer",
            "password",
        ]
