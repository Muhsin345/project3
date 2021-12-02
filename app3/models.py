from django.db import models

# Create your models here.
class student(models.Model):
    Name=models.CharField(max_length=50)
    Age=models.IntegerField()
    DOJ=models.DateField()
    Place=models.CharField(max_length=100)
    Username=models.CharField(max_length=50,default=None)
    Password=models.CharField(max_length=20,default=None)
class employees(models.Model):
    Name=models.CharField(max_length=50)
    Gender=models.CharField(max_length=20)
    Email=models.EmailField()
    # Address=models.CharField(max_length=200)
class up_file(models.Model):
    Name=models.CharField(max_length=100)
    Filename=models.CharField(max_length=100)
class ajax(models.Model):
    Name=models.CharField(max_length=100)
    Address=models.CharField(max_length=100)
    E_mail=models.CharField(max_length=100)