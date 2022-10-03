from django.urls import path

from .views import AllDispatches


urlpatterns = [
    path("", AllDispatches.as_view(), name="all-dispatch-list"),
]