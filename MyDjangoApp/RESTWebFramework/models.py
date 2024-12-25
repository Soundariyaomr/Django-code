from django.db import models


# Create your models here.
class EmployeeRegisterModel(models.Model):
    empId = models.IntegerField()
    name = models.CharField(max_length=15)
    phno = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return self.name
