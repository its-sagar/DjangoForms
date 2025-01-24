from django import forms
from .models import Employee, Position

class EmployeeForm(forms.ModelForm):
    gender = [
        ("Male", "Male"),
        ("Female", "Female"),
        ("Other", "Other"),
    ]

    Name = forms.CharField(
        max_length=50,
        label="Employee Name",
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control shadow-sm rounded-pill',
            'placeholder': 'Enter Employee Name',
        })
    )

    Email = forms.EmailField(
        label="Employee Email",
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'form-control shadow-sm rounded-pill',
            'type': 'email',
            'placeholder': 'example@example.com',
        })
    )

    Gender = forms.ChoiceField(
        label="Gender",
        choices=gender,
        required=True,
        widget=forms.Select(attrs={
            'class': 'form-select shadow-sm rounded-pill',
            'placeholder': 'Select Gender',
        })
    )

    Position = forms.ModelMultipleChoiceField(
        queryset=Position.objects.all(),
        widget=forms.CheckboxSelectMultiple(attrs={
            'class': 'position-checkbox',
        })
    )

    class Meta:
        model = Employee
        fields = [
            'Name',
            'Email',
            'Gender',
            'Position',
        ]

    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['style'] = 'margin-bottom: 15px;'
