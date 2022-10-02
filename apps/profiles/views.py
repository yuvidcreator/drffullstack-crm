from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.accounts.models import User
from apps.accounts.serializers import UserSerializer

from .exceptions import NotYourProfile, ProfileNotFound
from .models import Employee, Customer
from .renderers import EmployeeJSONRenderer, CustomerJSONRenderer
from .serializers import (EmployeeSerializer, UpdateEmployeeSerializer, CustomerSerializer, UpdateCustomerSerializer)

# Create your views here.


class CustomerListAPIView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = User.objects.filter(is_customer=True)
    serializer_class = UserSerializer


"""
    # Function Base API View
    from rest_framework import api_view, permissions
    @api_view(["GET"])
    @permission_classes((permissions.IsAuthenticated))
    def get_all_customers(request):
        customers = Profile.objects.filter(is_customer=True)
        serializer=ProfileSerializer(customers, many=True)
        name_spaced_response={"customers": serializer.data}
        return Response(name_spaced_response,status=status.HTTP_200_OK)
"""


class GetEmployeAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    renderer_classes = [EmployeeJSONRenderer]

    def get(self, request):
        user = self.request.user
        user_profile = Employee.objects.get(user=user)
        serializer = EmployeeSerializer(user_profile, context={"request": request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class UpdateEmployeeAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    renderer_classes = [EmployeeJSONRenderer]

    serializer_class = UpdateEmployeeSerializer

    def patch(self, request, pkid):
        try:
            Employee.objects.get(user_id=pkid)
        except Employee.DoesNotExist:
            raise ProfileNotFound

        user_id = request.user.pkid
        if user_id != pkid:
            raise NotYourProfile

        data = request.data
        serializer = UpdateEmployeeSerializer(
            instance=request.user.employee_profiles, data=data, partial=True
        )

        serializer.is_valid()
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
