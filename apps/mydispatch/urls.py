from django.urls import path

from .views import AllDispatches, DeliveryboyDispatchView


urlpatterns = [
    path("", AllDispatches.as_view(), name="all-dispatch-list"),
    path("delivery_boy_dispatchlist/", DeliveryboyDispatchView.as_view(),name = "delivery_boy_dispatchlist"),
]