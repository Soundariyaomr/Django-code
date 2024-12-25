import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MyDjangoApp.settings')

import django

django.setup()

from faker import Faker
from random import randint
from CRUDWebApp.models import EmployeeDetails

fake = Faker()


def fakeDetails():
    empId = randint(100, 200)
    empName = fake.name()
    empPhno = randint(8765434588, 9999999999)
    empEmail = fake.email()
    empAddress = fake.city()
    empSalary = randint(40000, 90000)

    EmployeeDetails.objects.get_or_create(emp_id=empId, emp_name=empName,
                                          emp_phno=empPhno, emp_email=empEmail, emp_address=empAddress,
                                          emp_salary=empSalary)


for i in range(10):
    fakeDetails()
