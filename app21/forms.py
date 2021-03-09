from django.forms import ModelForm
from .models import StudentModel

class EmployeeForm(ModelForm):
    class Meta:
        model=StudentModel
        fields='__all__'