from django import forms
from onetomany.models import Department, Employee

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = '__all__'

class EmployeeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.fields['departments'].queryset = Department.objects.all()

    class Meta:
        model = Employee
        fields = '__all__'