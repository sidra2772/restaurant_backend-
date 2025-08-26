from django.urls import path
from apps.restaurants.views.orders import (
    OrderListView, OrderDetailView,
    OrderItemListView, OrderItemDetailView,
)

app_name = 'orders'

urlpatterns = [
    path("orders/", OrderListView.as_view(), name="order-list"),
    path("orders/<int:id>/", OrderDetailView.as_view(), name="order-detail"),
    path("order-items/", OrderItemListView.as_view(), name="orderitem-list"),
    path("order-items/<int:id>/", OrderItemDetailView.as_view(), name="orderitem-detail"),
]
