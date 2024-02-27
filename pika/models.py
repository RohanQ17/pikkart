from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True, blank=True)
    name = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=100, null=True)
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    digital = models.BooleanField(default=False, null=True, blank=True)
    #image
    def __str__(self):
        return self.name
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL,null=True, blank=True)  # foreign key means one to many relationship that means that one user can have multiple orders
    date_order = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False, null=True, blank=True)
    transaction_id = models.CharField(max_length=200,null=True)

    def __str__(self):
        return str(self.id)

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL,null=True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL,null=True, blank=True)
    quantity = models.IntegerField(default=0,null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.name

class Shipping_Address(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL,null=True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True)
    city = models.CharField(max_length=100, null=True)
    state = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=100, null=True)
    postal_code = models.CharField(max_length=100, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.address




