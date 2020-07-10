from django.db import models

# Create your models here.


class Customer (models.Model):

    name = models.CharField(max_length=100, null= True)
    phone = models.CharField( max_length=50)
    email = models.EmailField( max_length=254)
    date_created= models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

class Product(models.Model):

    CATEGORY = (
        ('In Door', 'In Door'),
        ('Out Door', 'Out Door'),
    )

    name = models.CharField(max_length=50)
    price = models.FloatField()
    category = models.CharField(max_length=50, choices= CATEGORY)
    description = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True, null = True)

    def __str__(self):
        return self.name
    

class Order(models.Model):
    

    STATUS = (
        ('Pending', 'Pending'),
        ('Out for Delivery','Out for Delivery'),
        ('Delivered', 'Delivered'),
        )
    status = models.CharField(max_length=50, choices= STATUS)
    date_created = models.DateTimeField(auto_now_add=True, null = True)
    # customer =
    # product = 