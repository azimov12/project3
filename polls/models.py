from django.db import models

# Create your models here.
class Phones(models.Model):
    phone_name = models.CharField(max_length=32, default=''),
    phone_price = models.IntegerField(default=0)

class Headphones(models.Model):
    headphones_name = models.CharField(max_length=25, default=''),
    headphones_price = models.IntegerField(default=0)