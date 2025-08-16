from django.db import models
# Create your models here.
class Booking(models.Model):
    fname=models.CharField(max_length=20)
    lname=models.CharField(max_length=20)
    email=models.EmailField()
    phone=models.CharField(max_length=15)
    date=models.DateField()
    time=models.TimeField()

class Cancel_Booking(models.Model):
    lname=models.CharField(max_length=20)
    email=models.EmailField()
    phone=models.CharField(max_length=15)
    date=models.DateField()
    time=models.TimeField()

class Online_Order(models.Model):
    fname=models.CharField(max_length=20)
    lname=models.CharField(max_length=20)
    address=models.CharField(max_length=200)
    phone=models.CharField(max_length=15)
    payment=models.CharField(max_length=20,default="Cash")

class Cancel_Order(models.Model):
    fname=models.CharField(max_length=20)
    lname=models.CharField(max_length=20)
    email=models.EmailField()
    phone=models.CharField(max_length=15)
    date=models.DateField()
    time=models.TimeField()

class Userlogin(models.Model):
    us=models.CharField(max_length=20)
    ps=models.CharField(max_length=20)   

class Adminlogin(models.Model):
    us=models.CharField(max_length=20)
    ps=models.CharField(max_length=20)       

class register(models.Model):
    userid=models.CharField(max_length=20)
    name=models.CharField(max_length=20)
    mobile=models.CharField(max_length=15)
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=20)