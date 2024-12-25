from django.db import models


# Create your models here.
class EmployeeInfo(models.Model):
    empId = models.IntegerField()
    empName = models.CharField(max_length=15)
    empAddress = models.CharField(max_length=30)
    empPhno = models.IntegerField()

    def __str__(self):
        return self.empName


class StudentDetails(models.Model):
    regNo = models.IntegerField()
    name = models.CharField(max_length=15)
    phno = models.IntegerField()
    address = models.CharField(max_length=30)
    email = models.EmailField()
    courseName = models.CharField(max_length=10)
    totalFee = models.IntegerField()

    def __str__(self):
        return self.name
