from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from . import Form
from .models import RegisterModel


def register(request):
    form = Form.Registration
    return render(request, "FormWebApp\\register.html", context={"form": form})


def submitRegister(request):
    if request.method == "POST":

        if request.POST.get("FirstName") and request.POST.get("LastName") and request.POST.get(
                "Email") and request.POST.get("Password") and request.POST.get("DOB"):
            reg = RegisterModel()
            reg.FirstName = request.POST.get("FirstName")
            reg.LastName = request.POST.get("LastName")
            reg.Email = request.POST.get("Email")
            reg.Password = request.POST.get("Password")
            reg.DOB = request.POST.get("DOB")
            reg.save()
            return HttpResponse("Successfully User account is registered!")
        else:
            return HttpResponse("User account is not registered!")

    form = Form.Registration
    return render(request, "FormWebApp\\register.html", context={"form": form})


def registerdetails(request):
    reg = RegisterModel.objects.all()
    return render(request, 'FormWebApp\\userregister.html', context={"reg": reg})


def myform(request):
    form = Form.MyForm
    return render(request, "FormWebApp\\MyForm.html", context={"form": form})
