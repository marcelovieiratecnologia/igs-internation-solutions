from django.contrib import admin
from .models import Employee, Department


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name')

class EmployeesAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'department')


admin.site.register(Department)
admin.site.register(Employee, EmployeesAdmin)

