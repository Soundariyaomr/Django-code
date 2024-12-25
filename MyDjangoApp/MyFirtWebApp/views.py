from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def homepage(request):
    return render(request, r'FirstWebApp\HomePage.html')


def loginpage(request):
    return render(request, r'FirstWebApp\Login.html')


def registerpage(request):
    return render(request, r'FirstWebApp\Register.html')
