from email.policy import default
from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Phone(models.Model):
    phone_number = models.CharField(max_length=30)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.phone_number