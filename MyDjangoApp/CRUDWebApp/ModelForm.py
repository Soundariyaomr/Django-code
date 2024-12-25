from django.forms import ModelForm

from .models import EmployeeDetails


class EmployeeModelForm(ModelForm):
    class Meta:
        model = EmployeeDetails
        fields = "__all__"
