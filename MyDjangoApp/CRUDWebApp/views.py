from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from .ModelForm import EmployeeModelForm
from .models import EmployeeDetails


def employeeinfo(request):
    emp = EmployeeDetails.objects.all()
    # to convert object into json
    data = serializers.serialize("json", emp)
    return HttpResponse(data, content_type="application/json")
    # return render(request, "CRUDWebApp\\EmployeeInfo.html", context={"emp": emp})


def createEmployeeRegister(request):
    empinfo = EmployeeModelForm()
    if request.method == "POST":
        form = EmployeeModelForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse(
                "New User account successfully created!<a href='/curd/empInfo/'>Click Here</a>")

    return render(request, "CRUDWebApp\\CreateEmployee.html", context={"empinfo": empinfo})


def deleteEmployee(request, id):
    emp = EmployeeDetails.objects.get(id=id)
    emp.delete()
    # return HttpResponse("User Registered successfully deleted<a href='/curd/empInfo/'>Click Here!</a>")
    # return redirect("/curd/empInfo/")
    return redirect("/home/")


def udpateEmployee(request, id):
    empdetails = EmployeeDetails.objects.get(id=id)
    if request.method == "POST":
        form = EmployeeModelForm(request.POST, instance=empdetails)
        if form.is_valid():
            form.save()
            return HttpResponse(
                "User data successfully updated!<a href='/curd/empInfo/'>Click Here</a>")

    return render(request, "CRUDWebApp\\UpdateEmployee.html", context={"emp": empdetails})
