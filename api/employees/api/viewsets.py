from rest_framework import viewsets
from employees.api import serializers
from employees import models


class EmployeesViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.EmployeesSerializer
    queryset = models.Employee.objects.all()

