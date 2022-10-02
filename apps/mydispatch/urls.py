from django.urls import path

from .views import MyAllDispatchAPIView


urlpatterns = [
    path("all/", MyAllDispatchAPIView.as_view(), name="all-dispatch-list"),
]