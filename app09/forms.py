from django import forms
from .models import Employee

class EmployeeForm(forms.Form):
    gender_choice = [
        ("Male","Male"),
        ("Female","Female"),
        ("Other","Other")
    ]

    Name = forms.CharField(
        label="Employee Name",
        max_length=50,
        required=True,
        widget=forms.TextInput(attrs={
            'class':'form-control',
            'placeholder':'Enter Emplooye Name',
        })
    )

    Salary = forms.IntegerField(
        min_value=0,
        max_value=10000,
        label="Employee Salary",
        required=True,
        widget=forms.NumberInput(attrs={
            'class':'form-control',
            'placeholder':'Enter Employee Salary',
        })
    )

    Gender = forms.ChoiceField(
        label="Employee Gender",
        choices=gender_choice,
        required=True,
        widget=forms.Select(attrs={
            'class':'form-control'
        })
    )