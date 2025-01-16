from django import forms

class EmployeeForm(forms.Form):

    Name = forms.CharField(
        max_length=50,
        label = "Employee Name",
        required = True,
        widget = forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder' : 'Enter Your Name'
        }),
        # initial = "Name",
        # help_text = "Please Enter Your Full Name"
    )

    Salary = forms.IntegerField(
        min_value = 0,
        max_value = 10000,
        label = "Employee Salary",
        required = True,
        widget = forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder' : 'Enter Employee Salary'
        }),
    )

    Score = forms.FloatField(
        min_value = 0.0,
        max_value = 10.0,
        label = "Employee Score",
        required = True,
        widget = forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder' : 'Enter Employee Score between 0 to 10'
        }),
    )