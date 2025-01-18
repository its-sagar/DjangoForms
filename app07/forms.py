from django import forms

class EmployeeForm(forms.Form):
    Name = forms.CharField(
        max_length=50,
        label= "Employee Name",
        required=True,
        widget = forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter Employee Name'
        })
    )

    File = forms.FileField(
        label = "Upload File",
        required = True,
        widget = forms.ClearableFileInput(attrs={
            'class': 'form-control'
        })
    )