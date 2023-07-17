from django.db import models


# Create your models here.


class Employee_details(models.Model):
    name=models.CharField(max_length=30)
    email=models.CharField(max_length=20)
    address=models.CharField(max_length=100)
    department=models.CharField(max_length=50)
    phone=models.IntegerField(max_length=10)
    positions=models.CharField(max_length=100)
