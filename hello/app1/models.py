from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Employees(models.Model):

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    # id = models.AutoField()
    name = models.CharField(max_length=250)
    age = models.IntegerField(default=18)
    email = models.EmailField()
    address = models.TextField(null=True, blank=True)
    photo = models.ImageField(null=True, upload_to="photos")
    
# class Department(models.Model):
#     dept = models.CharField(max_length=200)
#      project = models.TextField()
#     tech = models.CharField(max_length=100)
#     duration = models.IntegerField(default=3)


    # def __str__(self) -> str:
    #     return self.dept, self.project, self.tech, self.duration0      #this is for printing the object
