from django.shortcuts import render
from django.http import HttpResponse
from .models import Employee
from .forms import EmployeeForm

# Create your views here.

def employeeData(request):
    form = EmployeeForm()
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["Name"]
            salary = form.cleaned_data["Salary"]
            gender = form.cleaned_data["Gender"]

            employee = Employee(
                Name=name,
                Salary=salary,
                Gender=gender
            )

            employee.save()

            return HttpResponse("Data is saved in database successfully.")

    return render(request, 'app09/employee_form.html', {"form":form})