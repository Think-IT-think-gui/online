from django.db import models

# Create your models here.
class Login_info(models.Model):
    User = models.CharField(max_length=100)
    Password = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.User


class SignUp_info(models.Model):
    User = models.CharField(max_length=100)
    Password = models.CharField(max_length=100)
    First_Name = models.CharField(max_length=100)
    Gender = models.CharField(max_length=100)
    Location = models.CharField(max_length=100)
    Email = models.EmailField(max_length=100)
    Img = models.CharField(max_length=100, null=True )
    date = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.User

class Cart_info(models.Model):
    Product = models.CharField(max_length=100)
    Ammount = models.CharField(max_length=100)
    Quantity = models.CharField(max_length=100)
    User = models.CharField(max_length=100)
    Status = models.CharField(max_length=100)
    Description = models.CharField(max_length=500)
    date = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.Product


class Products(models.Model):
    Product = models.CharField(max_length=100)
    Ammount = models.CharField(max_length=100)
    Class = models.CharField(max_length=100)
    Image = models.TextField(max_length=500, null=True)
    Description = models.CharField(max_length=500)
    Rate = models.CharField(max_length=500)
    Delivery_method = models.CharField(max_length=500)
    date = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.Product

class Admin(models.Model):
    User = models.CharField(max_length=100)
    Password = models.CharField(max_length=100)
    First_Name = models.CharField(max_length=100)
    Last_Name = models.CharField(max_length=100)
    Location = models.CharField(max_length=100)
    Email = models.EmailField(max_length=100)
    date = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.User


class Contact(models.Model):
    User = models.CharField(max_length=100)
    Message = models.CharField(max_length=100)
    Email = models.EmailField(max_length=100)
    date = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.User
