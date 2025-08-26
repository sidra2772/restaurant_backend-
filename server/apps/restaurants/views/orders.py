from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from apps.restaurants.models import Orders, OrderItem
from apps.restaurants.serializers import OrderSerializer, OrderItemSerializer


# Order Views
class OrderListView(ListAPIView, CreateAPIView):
    """
    List all orders OR create a new order.
    """
    serializer_class = OrderSerializer
    queryset = Orders.objects.all()


class OrderDetailView(RetrieveAPIView, UpdateAPIView, DestroyAPIView):
    """
    Retrieve, update, or delete a single order by ID.
    """
    serializer_class = OrderSerializer
    queryset = Orders.objects.all()
    lookup_field = "id"


# Order Items
class OrderItemListView(ListAPIView, CreateAPIView):
    """
    List all order items OR create a new order item.
    """
    serializer_class = OrderItemSerializer
    queryset = OrderItem.objects.all()


class OrderItemDetailView(RetrieveAPIView, UpdateAPIView, DestroyAPIView):
    """
    Retrieve, update, or delete a single order item by ID.
    """
    serializer_class = OrderItemSerializer
    queryset = OrderItem.objects.all()
    lookup_field = "id"
