from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Vehicle(models.Model):
    FUEL_TYPE = [
        ('petrol','Petrol'),
        ('diesel','Diesel'),
        ('electric','Electric'),
        ('hybrid','Hybrid')
    ]
    name = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
    year = models.IntegerField()
    price_per_day = models.DecimalField(max_digits=10, decimal_places=2)
    fuel_type = models.CharField(max_length=10,choices=FUEL_TYPE)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name 


class Booking(models.Model):
    vehicle = models.ForeignKey(Vehicle,on_delete=models.CASCADE,related_name='bookings')
    customer_name = models.CharField(max_length=50)
    customer_phone = models.CharField(max_length=13)
    start_date = models.DateField()
    end_date = models.DateField()
    total_amount = models.DecimalField(max_digits=10,decimal_places=2,blank=True)

    def __str__(self):
        return self.customer_name