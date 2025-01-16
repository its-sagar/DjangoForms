from django.shortcuts import render
from django.http import HttpResponse
from .models import Employee
from .forms import EmployeeForm

# Create your views here.

def employeeData(request):
    form = EmployeeForm()
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['Name']
            salary = form.cleaned_data['Salary']
            score = form.cleaned_data['Score']
            is_employee = form.cleaned_data['is_employee']
            empJoiningDate = form.cleaned_data['EmpJoiningDate']

            employee = Employee.objects.create(
                Name = name,
                Salary = salary,
                Score = score,
                is_employee = is_employee,
                EmpJoiningDate = empJoiningDate,
            )

            employee.save()
            return HttpResponse("Data Saved In Database Successfully.")
    return render(request, 'app04/employeeForm.html', {"form":form})


