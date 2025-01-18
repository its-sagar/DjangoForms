from django.shortcuts import render
from django.http import HttpResponse
from . models import Employee
from . forms import EmployeeForm


# Create your views here.

def employeeData(request):
    form = EmployeeForm()
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['Name']
            salary = form.cleaned_data['Salary']
            score = form.cleaned_data['Score']
            JoiningDateTime = form.cleaned_data['EmpJoiningDate']
            is_employee = form.cleaned_data['is_employee']

            employee = Employee(
                Name = name,
                Salary = salary,
                Score = score,
                EmpJoiningDate = JoiningDateTime,
                is_employee = is_employee
            )

            employee.save()
            return HttpResponse("Data is saved in the database successfully.")
    return render(request, 'app05/employeeForm.html', {'form':form})
