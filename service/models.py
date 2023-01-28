from django.db import models


# Create your models here.


class User(models.Model):
    email = models.EmailField(primary_key=True)
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=13)


class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=50)
    address = models.TextField()