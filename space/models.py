from django.db import models

# Create your models here.

class ParkingSpace(models.Model):
    space_name = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    availability = models.BooleanField(default=True)
    def __str__(self):
        return f"{self.space_name} - {self.location}"

