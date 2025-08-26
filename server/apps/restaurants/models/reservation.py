from django.db import models
from coresite.mixin import AbstractTimeStampModel
from apps.userprofile.models import UserProfile
from apps.restaurants.models import Restaurant    



# Table Model
class Table(AbstractTimeStampModel):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='tables')
    number = models.PositiveIntegerField()  # Table number
    seats = models.PositiveIntegerField(default=2)
    is_available = models.BooleanField(default=True)

    class Meta:
        unique_together = ('restaurant', 'number') 

    def __str__(self):
        return f"Table {self.number} - {self.restaurant.name}"

# Reservation Model
class Reservation(AbstractTimeStampModel):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
    )

    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='reservations')
    table = models.ForeignKey(Table, on_delete=models.CASCADE, related_name='reservations')
    reservation_date = models.DateField()
    reservation_time = models.TimeField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')

    class Meta:
        unique_together = ('table', 'reservation_date', 'reservation_time')  # prevent double booking

    def __str__(self):
        return f"{self.user.first_name} → Table {self.table.number} on {self.reservation_date} at {self.reservation_time}"
