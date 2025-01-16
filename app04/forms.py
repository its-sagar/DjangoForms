from django import forms
from .models import Employee

class EmployeeForm(forms.Form):
    Name = forms.CharField(
        max_length = 50,
        label = "Employee Name",
        required = True,
        widget = forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter Your Name'
        })

    )

    Salary = forms.IntegerField(
        label = 'Employee Salary',
        min_value = 0,
        max_value = 10000,
        required = True,
        widget = forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter Employee Salary'
        })
    )

    Score = forms.FloatField(
        label = 'Employee Score',
        min_value = 0.0,
        max_value = 10.0,
        required = True,
        widget = forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter Employee Score'
        })
    )

    EmpJoiningDate = forms.DateField(
        label = 'Joining Date',
        required = True,
        widget = forms.DateInput(attrs={
            'class': 'form-control',
            'type': 'date'
        }),
        initial = '2000-01-01'
    )

    is_employee = forms.BooleanField(
        label = "Is_Employee",
        required = True,
        widget = forms.CheckboxInput(attrs={
            'class': 'form-check-input',
        }),
    )

    