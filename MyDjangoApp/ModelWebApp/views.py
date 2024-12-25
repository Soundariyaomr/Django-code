from django.shortcuts import render

# Create your views here.
from .models import StudentDetails


def studinfo(request):
    info = StudentDetails.objects.all()
    std = {"details": info}
    return render(request, "ModelWebApp//stddetails.html", context=std)
