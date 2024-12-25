from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view

from RESTWebFramework.models import EmployeeRegisterModel

from RESTWebFramework.serializer import EmployeeRegisterSerializer
from rest_framework.response import Response


@api_view(["GET"])
def employeeregister(request):
    emp = EmployeeRegisterModel.objects.all()
    serializers = EmployeeRegisterSerializer(emp, many=True)
    return Response(serializers.data)


@api_view(["POST", "GET"])
def createregister(request):
    newuser = EmployeeRegisterSerializer(data=request.data)
    if newuser.is_valid():
        newuser.save()
    return Response(newuser.data)
