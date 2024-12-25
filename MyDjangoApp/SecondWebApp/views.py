from datetime import *

from django.shortcuts import render


# Create your views here.

def ipltable(request):
    date = datetime.now()
    d = {'name': 'greens', "country": "IND", "Location": "Chennai", "Date": date}
    return render(request, "SecondWebApp\\ipltable.html", context=d)


def productdetails(request):
    return render(request, "SecondWebApp\\productdetails.html")


def calculateproduct(request):
    mobile = int(request.GET["mobile"]) # name attribute
    laptop = int(request.GET["laptop"])
    keyboard = int(request.GET["keyboard"])
    mouse = int(request.GET["mouse"])
    total = mobile + laptop + keyboard + mouse
    res1 = {"res": total}
    return render(request, "SecondWebApp\\result.html", context=res1)
