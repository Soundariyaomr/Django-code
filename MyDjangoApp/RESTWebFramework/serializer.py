from rest_framework import serializers

from RESTWebFramework.models import EmployeeRegisterModel


class EmployeeRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeRegisterModel
        fields = "__all__"
