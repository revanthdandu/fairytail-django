from django.db import models


class Addantique(models.Model):
    image = models.ImageField(upload_to='antiquepics')
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    place = models.CharField(max_length=200)
    enddate = models.DateField()

