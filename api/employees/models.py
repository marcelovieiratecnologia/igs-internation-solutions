from random import choices
from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=25, blank=False, null=False)

    def __str__(self):
        return self.name

class Employee(models.Model):

    # DEPARTMENT_CHOICES = (
    #     ("Tester","Tester"),
    #     ("RH","RH"),
    #     ("Developer","Developer"),
    # )
    
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=70, blank=False, null=False, unique=True)
    department = models.ForeignKey(Department, on_delete=models.DO_NOTHING)
    # department = models.CharField(max_length=20, choices=DEPARTMENT_CHOICES, blank=False, null=False)

    def __str__(self):
        return self.name