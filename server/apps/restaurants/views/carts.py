from django.forms import ValidationError
from rest_framework import viewsets, permissions
from apps.restaurants.models import Cart, CartItem
from apps.restaurants.serializers.carts import CartItemSerializer, CartSerializer 



# Cart viewset
class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [permissions.IsAuthenticated]
    # Override get_queryset to filter carts by the authenticated user
    def get_queryset(self):
        user = self.request.user
        return Cart.objects.filter(user=user)
    # Override perform_create to set the user on the cart
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

# CartItem viewset
class CartItemViewSet(viewsets.ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    # Override get_queryset to filter cart items by the authenticated user
    def get_queryset(self):
        user = self.request.user
        return CartItem.objects.filter(cart__user=user)
    # Override perform_create to associate the cart item with the user's cart
   
    def perform_create(self, serializer):
        cart_id = self.request.data.get("cart")
        if not cart_id:
            raise ValidationError({"cart": "Cart ID is required."})

        try:
            cart = Cart.objects.get(id=cart_id, user=self.request.user)
        except Cart.DoesNotExist:
            raise ValidationError({"cart": "Invalid cart for this user."})

        serializer.save(cart=cart)
