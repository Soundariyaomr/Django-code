from django.contrib import admin

# Register your models here.
from .models import EmployeeInfo, StudentDetails

admin.site.register(EmployeeInfo)
admin.site.register(StudentDetails)