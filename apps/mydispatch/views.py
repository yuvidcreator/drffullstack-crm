from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.mydispatch.models import Dispatch
from apps.mydispatch.serializers import MyDispatcherializer
from apps.mydispatch.pagination import MyDisptachListPagination
# Create your views here.



# class MyAllDispatchAPIView(generics.ListAPIView):
#     permission_classes = [permissions.AllowAny]
#     queryset = Dispatch.objects.all()
#     serializer_class = MyDispatcherializer

class AllDispatches(APIView):
    permission_classes = [permissions.AllowAny]
    pagination_class = MyDisptachListPagination

    def get(self, request):
        mydispatch = Dispatch.objects.all()
        serializer = MyDispatcherializer(mydispatch, many=True)
        return Response({"dispatchdata": serializer.data}, status=status.HTTP_200_OK)