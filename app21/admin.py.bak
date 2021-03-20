from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import StudentModel


# Register your models here.
class EmployeeAdmin(ModelAdmin):
    list_display = ['name', 'age']
    ordering = ['name',]


admin.site.register(StudentModel, EmployeeAdmin)
