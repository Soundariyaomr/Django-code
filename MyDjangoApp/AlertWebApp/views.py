from django.contrib import messages
from django.shortcuts import render


# Create your views here.
def showdata(request):
    return render(request, "AlertWebApp\\alert.html")


def success(request):
    messages.success(request, "This is Success Message")
    return render(request, "AlertWebApp\\alert.html")


def error(request):
    messages.error(request, "This is Error Message")
    return render(request, "AlertWebApp\\alert.html")


def warning(request):
    messages.warning(request, "This Warning message")
    return render(request, "AlertWebApp\\alert.html")


def info(request):
    messages.info(request, "This is information message")
    return render(request, "AlertWebApp\\alert.html")
