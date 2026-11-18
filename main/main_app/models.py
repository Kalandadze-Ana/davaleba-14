from django.db import models


class Customer(models.Model):
    first_name = models.CharField()
    last_name = models.CharField()
    email = models.EmailField()
    city = models.CharField()
    age = models.IntegerField()
    created_at = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"



class Product(models.Model):
    name = models.CharField()
    category = models.CharField()
    price = models.DecimalField()
    stock = models.IntegerField()
    is_available = models.BooleanField(default=True)
    added_at = models.DateField()

    def __str__(self):
        return self.name


class Cart(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.customer} - {self.product} x {self.quantity}"
