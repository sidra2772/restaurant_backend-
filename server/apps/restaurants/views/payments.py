from rest_framework import viewsets, permissions
from apps.restaurants.models import PaymentDetails
from server.apps.restaurants.serializers.payments import PaymentDetailsSerializer


# Admin: Full access to all payments
class PaymentDetailsAdminViewSet(viewsets.ModelViewSet):
    queryset = PaymentDetails.objects.all()
    serializer_class = PaymentDetailsSerializer
    permission_classes = [permissions.IsAdminUser]


# User: Only their own payment details
class PaymentDetailsUserViewSet(viewsets.ModelViewSet):
    serializer_class = PaymentDetailsSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return PaymentDetails.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Automatically assign logged-in user
        serializer.save(user=self.request.user)
