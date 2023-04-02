from django.test import TestCase

# Create your tests here.


def get_cart_items (self):
    orderitems= self.orderitems_set.all()
    total = sum([item.quantity for item in orderitems])
    return total