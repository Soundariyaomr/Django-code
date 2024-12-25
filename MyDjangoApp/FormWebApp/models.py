from django.db import models


# Create your models here.
class RegisterModel(models.Model):
    FirstName = models.CharField(max_length=15)
    LastName = models.CharField(max_length=15)
    Email = models.EmailField()
    Password = models.CharField(max_length=15)
    DOB = models.CharField(max_length=20)

    def __str__(self):
        return self.FirstName
