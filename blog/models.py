from django.db import models

# Create your models here.
class Test(models.Model):
    name = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    data = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    rate = models.CharField(max_length=255)
    comments = models.CharField(max_length=255)
