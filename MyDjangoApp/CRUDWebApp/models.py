from django.db import models


# Create your models here.

class EmployeeDetails(models.Model):
    emp_id = models.IntegerField()
    emp_name = models.CharField(max_length=15)
    emp_phno = models.IntegerField()
    emp_email = models.EmailField()
    emp_address = models.CharField(max_length=30)
    emp_salary = models.IntegerField()

    def __str__(self):
        return self.emp_name
