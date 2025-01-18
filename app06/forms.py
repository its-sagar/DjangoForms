from django import forms


class EmployeeForm(forms.Form):
    Name = forms.CharField(
        max_length=50,
        label="Employee Name",
        required=True,
        widget = forms.TextInput(attrs= {
            'class': 'form-control',
            'placeholder': 'Enter Your Name'
        }),
    )

    Email = forms.EmailField(
        label="Employee Email",
        required=True,
        widget = forms.EmailInput(attrs={
            'class': 'form-control',
            'type': 'email',
            'placeholder': 'Enter Your Email',
        })
    )

    Salary = forms.IntegerField(
        min_value = 0,
        max_value = 10000,
        label = 'Employee Salary',
        required = True,
        widget = forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter Your Salary'
        })
    )

    Score = forms.FloatField(
        min_value = 0.0,
        max_value = 10.0,
        label = 'Employee Score',
        required = True,
        widget = forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter Your Score'
        })
    )

    EmpJoiningDate = forms.DateField(
        label= 'Joining Date',
        required= True,
        widget= forms.DateInput(attrs={
            'class': 'form-control',
            'type': 'date'
        }),
        initial = '2000-01-01'
    )

    is_employee = forms.BooleanField(
        label= 'Is_Employee',
        required= True,
        widget = forms.CheckboxInput(attrs={
            'class': 'form-check-input',
        })
    )