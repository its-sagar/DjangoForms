from django.shortcuts import render
from .forms import EmployeeForm
from .models import Employee

# Create your views here.

def employeeData(request):
    form = EmployeeForm()
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['Name']
            salary = form.cleaned_data['Salary']
            score = form.cleaned_data['Score']

            employee = Employee.objects.create(
                Name = name,
                Salary = salary,
                Score = score
            )

            employee.save()
            return render(request, 'home.html')

    return render(request, 'app02/employeeForm.html', {"form":form})
