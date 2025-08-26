from django.urls import path
from apps.restaurants.views.payments import (
    PaymentDetailsAdminViewSet,
    PaymentDetailsUserViewSet
)

name_app = 'payments'


urlpatterns = [
    path('admin/payments/', PaymentDetailsAdminViewSet.as_view({'get': 'list', 'post': 'create'}), name='admin-payment-list'),
    path('user/payments/', PaymentDetailsUserViewSet.as_view({'get': 'list', 'post': 'create'}), name='user-payment-list'),
]
