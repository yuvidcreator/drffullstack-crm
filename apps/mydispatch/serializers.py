from rest_framework import serializers
from apps.mydispatch.models import Dispatch
from apps.profiles.models import Employee, Customer




class MyDispatcherializer(serializers.ModelSerializer):
    class Meta:
        model = Dispatch
        fields = "__all__"
        depth = 1