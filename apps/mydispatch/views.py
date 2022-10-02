from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.mydispatch.models import Dispatch
from apps.mydispatch.serializers import MyDispatcherializer
# Create your views here.


class MyAllDispatchAPIView(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Dispatch.objects.all()
    serializer_class = MyDispatcherializer
