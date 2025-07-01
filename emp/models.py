from django.db import models

# Create your models here.

class Employee(models.Model):
    employee_id= models.CharField(max_length=100)
    Name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    phone_nuber=models.CharField(max_length=50)


