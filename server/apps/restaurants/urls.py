
from django.urls import path, include
from django.urls import re_path
from .views import MenuListView,MenuDetailView, MenuItemListView, MenuItemDetailView, RestaurantListView, RestaurantDetailView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('restaurants/', RestaurantListView.as_view(), name='restaurant-list'),
    path('restaurants/<int:id>/', RestaurantDetailView.as_view(), name='restaurant-detail'),
    path('restaurants/<int:restaurant_id>/menus/', MenuListView.as_view(), name='menu-list'),
    path('restaurants/<int:restaurant_id>/menus/<int:id>/', MenuDetailView.as_view(), name='menu-detail'),
    path('menus/<int:menu_id>/menu-items/', MenuItemListView.as_view(), name='menu-item-list'),
    path('menus/<int:menu_id>/menu-items/<int:id>/', MenuItemDetailView.as_view(), name='menu-item-detail'),
    path('carts/', include('apps.restaurants.urls.carts', namespace="carts")),
    path('orders/', include('apps.restaurants.urls.orders', namespace="orders")),
    path('payments/', include('apps.restaurants.urls.payments', namespace="payments")),

]
