from django import forms
from .models import Employee

class EmployeeForm(forms.Form):
    Name = forms.CharField()
    Salary = forms.IntegerField()