from django.db import models
from django.forms import CharField

# Create your models here.

class sec(models.Model):
    room_number = models.CharField(max_length=50)
    amount_paid = models.IntegerField()
    occupants_name = models.CharField(max_length=100)
    occupants_email = models.EmailField(max_length=254)
    occupants_occupation = models.CharField(max_length=50)
    number_of_nights = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
 
    def __str__(self):
        return self.room_number