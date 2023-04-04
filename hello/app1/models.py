from django.db import models

# Create your models here.

class Employees(models.Model):
    # id = models.AutoField()
    name = models.CharField(max_length=250)
    age = models.IntegerField(default=18)
    email = models.EmailField()
    phone = models.BigIntegerField()
    address = models.TextField(null=True, blank=True)
    photo = models.ImageField()
    
class Department(models.Model):
    dept = models.CharField(max_length=200)
    project = models.TextField()
    tech = models.CharField(max_length=100)
    duration = models.IntegerField(default=3)

