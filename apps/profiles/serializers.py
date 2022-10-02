from rest_framework import serializers

from apps.profiles.models import Employee, Customer


class EmployeeSerializer(serializers.ModelSerializer):
    user_pkid = serializers.CharField(source="user.pkid")
    user_id = serializers.UUIDField(source="user.id")
    first_name = serializers.CharField(source="user.first_name")
    last_name = serializers.CharField(source="user.last_name")
    full_name = serializers.SerializerMethodField(read_only=True)
    username = serializers.CharField(source="user.username")
    email = serializers.CharField(source="user.email")
    mobile = serializers.CharField(source="user.mobile")
    employee_status = serializers.SerializerMethodField("get_employee_status")
    is_active = serializers.BooleanField(source="user.is_active")
    is_staff = serializers.BooleanField(source="user.is_staff")
    is_superuser = serializers.BooleanField(source="user.is_superuser")
    is_employee = serializers.BooleanField(source="user.is_employee")    

    class Meta:
        model = Employee
        fields = [
            "pkid",
            "id",
            "user_pkid",
            "user_id",
            "username",
            "email",
            "mobile",
            "first_name",
            "last_name",
            "full_name",
            "profile_picture",
            "date_of_birth",
            "gender",
            "emp_id",
            "about_me",
            "eduaction",
            "work_experience",
            "pan_no",
            "bank_details",
            "salary",
            "address_line1",
            "address_line2",
            "city",
            "zip_code",
            "state",
            "country",
            "is_mobile_verified",
            "employee_status",
            "is_active",
            "is_staff",
            "is_superuser",
            "is_employee",
            # "is_customer",
            "is_admin",
            "is_manager",
            "is_accountant",
            "is_salesman",
            "is_deliveryboy",
            "top_employee",
            "rating",
            "num_reviews",
        ]
        depth = 1

    def get_full_name(self, obj):
        first_name = obj.user.first_name.title()
        last_name = obj.user.last_name.title()
        return f"{first_name} {last_name}"

    def get_employee_status(self, obj):
        status = obj.status
        return status

    def to_represenatation(self, instance):
        represenatation = super().to_represenatation(instance)
        if instance.is_staff:
            represenatation["is_staff"] = True
        if instance.is_superuser:
            represenatation["is_superuser"] = True
        if instance.is_employee:
            represenatation["is_employee"] = True
        return represenatation


class UpdateEmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        exclude = [
            "id"
        ]




class CustomerSerializer(serializers.ModelSerializer):
    pkid = serializers.CharField(source="user.pkid")
    id = serializers.UUIDField(source="user.id")
    first_name = serializers.CharField(source="user.first_name")
    last_name = serializers.CharField(source="user.last_name")
    full_name = serializers.SerializerMethodField(read_only=True)
    username = serializers.CharField(source="user.username")
    email = serializers.CharField(source="user.email")
    mobile = serializers.CharField(source="user.mobile")
    about_me = serializers.CharField()
    is_active = serializers.BooleanField(source="user.is_active")
    is_staff = serializers.BooleanField(source="user.is_staff")
    is_superuser = serializers.BooleanField(source="user.is_superuser")
    # is_employee = serializers.BooleanField(source="user.is_employee")
    is_customer = serializers.BooleanField(source="user.is_customer")
    # is_admin = serializers.BooleanField(source="user.is_admin")
    # is_manager = serializers.BooleanField(source="user.is_manager")
    # is_accountant = serializers.BooleanField(source="user.is_accountant")
    # is_salesman = serializers.BooleanField(source="user.is_salesman")
    # is_deliveryboy = serializers.BooleanField()

    class Meta:
        model = Customer
        fields = [
            "pkid",
            "id",
            "username",
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
            "is_mobile_verified",
            "is_verified_customer",
            "is_active",
            "is_staff",
            # "is_employee",
            "is_customer",
            "business_name",
            "business_wano",
            "business_address_line_1",
            "business_address_line_2",
            "business_area_name",
            "landmark",
            "directions_to_reach",
            "latitude",
            "longitude",
            "biz_googlemap_link",
            "business_zip_code",
            "business_city",
            "business_state",
            "business_country",
            "about_business",
            "upi_id",
            "adhaar_certificate1",
            "adhaar_certificate2",
            "gst_no",
            "gst_certificate",
            "pan_no",
            "pan_certificate",
            "security_cheque",
            "visiting_card",
            "bank_details",
            "status",
            "top_customer",
            "rating",
            "num_reviews",
        ]

    def get_full_name(self, obj):
        first_name = obj.user.first_name.title()
        last_name = obj.user.last_name.title()
        return f"{first_name} {last_name}"

    def to_represenatation(self, instance):
        represenatation = super().to_represenatation(instance)
        # if instance.is_staff:
        #     represenatation["is_staff"] = True
        if instance.is_customer:
            represenatation["is_customer"] = True
        return represenatation


class UpdateCustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        exclude = [
            "id",
            "pkid"
        ]