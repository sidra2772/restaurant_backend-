from django.db import models
from coresite.mixin import AbstractTimeStampModel


class OrderItem(AbstractTimeStampModel):
    menu_item = models.ForeignKey('restaurants.MenuItem', on_delete=models.CASCADE, related_name='menu_item_order_items')
    quantity = models.PositiveIntegerField(default=1)
    comments = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.menu_item.name + ' - ' + str(self.quantity) + ' pcs'

    class Meta:
        db_table = 'order_items'
        verbose_name = 'Order Item'
        verbose_name_plural = 'Order Items'


PAYMENT_STATUS = (
    ('Pending', 'Pending'),
    ('Confirmed', 'Confirmed'),
    ('Cancelled', 'Cancelled'),
)


class Orders(AbstractTimeStampModel):
    user = models.ForeignKey('userprofile.UserProfile', on_delete=models.CASCADE,related_name='userOrders')
    items = models.ManyToManyField('restaurants.OrderItem')
    ordered_date = models.DateTimeField(null=True,blank=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2,default=0)
    billing_first_name = models.CharField(max_length=255)
    billing_last_name = models.CharField(max_length=255)
    billing_email = models.EmailField()
    billing_phone = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    ordered = models.BooleanField(default=False)
    payment_status = models.CharField(max_length=255, default='Pending', choices=PAYMENT_STATUS)
    order_cancelled = models.BooleanField(default=False)
    billing_address = models.CharField(null=True,blank=True,max_length=500)
    shipping_address = models.CharField(null=True,blank=True,max_length=500)
    being_delivered = models.BooleanField(default=False)
    received = models.BooleanField(default=False)

    class Meta:
        db_table = 'orders'
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'
