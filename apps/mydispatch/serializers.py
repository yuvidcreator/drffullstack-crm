from rest_framework import serializers
from apps.mydispatch.models import Dispatch
from apps.profiles.models import Employee, Customer




class MyDispatcherializer(serializers.ModelSerializer):
    class Meta:
        model = Dispatch
        fields = "__all__"
        depth = 2



class DeliveryBoyDispatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = [
            "id",
            "pkid",
            "dispatch_order_id",
            "invoice_no",
            "party_name",
            "customer_mobile",
            "product",
            "total_price",
            "bill_status",
            "delivered_man",
            "delivery_date",
            "dispatch_status",
            "recieved_status",
            "payment_method",
            "remark",
            "created_at",
            "updated_at",
        ]
        depth = 2