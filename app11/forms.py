from django import forms
from .models import Employee

class EmployeeForm(forms.Form):
    Username = forms.CharField(
        max_length=50,
        label="Username",
        required=True,
        widget=forms.TextInput(attrs={
            'class':'form-control',
            'placeholder':'Enter Employee Name'
        })
    )

    Password = forms.CharField(
        max_length=50,
        label="Password",
        required=True,
        widget=forms.PasswordInput(attrs={
            'class':'form-control',
            'type':'Password'
        })
    )