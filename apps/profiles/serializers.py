from rest_framework import serializers

from apps.profiles.models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    pkid = serializers.CharField(source="user.pkid")
    id = serializers.UUIDField(source="user.id")
    first_name = serializers.CharField(source="user.first_name")
    last_name = serializers.CharField(source="user.last_name")
    full_name = serializers.SerializerMethodField(read_only=True)
    email = serializers.CharField(source="user.email")
    mobile = serializers.CharField(source="user.mobile")
    about_me = serializers.CharField()
    is_active = serializers.BooleanField(source="user.is_active")
    is_superuser = serializers.BooleanField(source="user.is_superuser")
    is_mainadmin = serializers.BooleanField(source="user.is_mainadmin")
    is_manager = serializers.BooleanField(source="user.is_manager")
    is_accountant = serializers.BooleanField(source="user.is_accountant")
    is_salesman = serializers.BooleanField(source="user.is_salesman")
    is_deliveryboy = serializers.BooleanField()

    class Meta:
        model = Profile
        fields = [
            "pkid",
            "id",
            "email",
            "mobile",
            "first_name",
            "last_name",
            "full_name",
            "profile_picture",
            "date_of_birth",
            "gender",
            "about_me",
            "address_line_1",
            "address_line_2",
            "city",
            "zip_code",
            "state",
            "country",
            "about_me",
            "is_mobile_verified",
            "is_active",
            "is_superuser",
            "is_mainadmin",
            "is_manager",
            "is_accountant",
            "is_salesman",
            "is_deliveryboy",
            "is_employee",
        ]

    def get_full_name(self, obj):
        first_name = obj.user.first_name.title()
        last_name = obj.user.last_name.title()
        return f"{first_name} {last_name}"

    def to_represenatation(self, instance):
        represenatation = super().to_represenatation(instance)
        if instance.is_deliveryboy:
            represenatation["is_deliveryboy"] = True
        if instance.is_employee:
            represenatation["is_employee"] = True
        return represenatation


class UpdateProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = [
            "profile_picture",
            "date_of_birth",
            "gender",
            "address_line_1",
            "address_line_2",
            "city",
            "zip_code",
            "state",
            "country",
            "about_me",
        ]
