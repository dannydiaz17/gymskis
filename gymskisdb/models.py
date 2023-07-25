from django.db import models
from datetime import date

# Create your models here.

class gym(models.Model):

    name        = models.CharField(max_length=50)
    address     = models.CharField(max_length=200)
    phone       = models.CharField(max_length=10)
    category    = models.CharField(max_length=50)
    rating      = models.FloatField()
    date_added  = models.DateField("date_added")
    promotion   = models.BooleanField(default=False)

#   def __init__(self):
#       self.date_added = date.today()
