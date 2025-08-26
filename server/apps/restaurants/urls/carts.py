from django.urls import path
from apps.restaurants.views.carts import CartViewSet, CartItemViewSet


name_app='cart'

urlpatterns = [
    path("carts/", CartViewSet.as_view({"get": "list", "post": "create"}), name="cart-list"),
    path("carts/<int:pk>/", CartViewSet.as_view({"get": "retrieve", "put": "update", "delete": "destroy"}), name="cart-detail"),
    path("cart-items/", CartItemViewSet.as_view({"get": "list", "post": "create"}), name="cartitem-list"),
    path("cart-items/<int:pk>/", CartItemViewSet.as_view({"get": "retrieve", "put": "update", "delete": "destroy"}), name="cartitem-detail"),
]
