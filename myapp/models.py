from django.db import models
class ca(models.Model):
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    date = models.DateField()

class login(models.Model):
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    date = models.DateField()

class register(models.Model):
    username = models.CharField(max_length=100)
    college = models.CharField(max_length=100)
    year = models.CharField(max_length=100)
    dob = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    referral = models.CharField(max_length=100)
# Create your models here.
