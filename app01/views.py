from django.shortcuts import render
from django.http import HttpResponse
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

            employee = Employee.objects.create(Name=name, Salary=salary)
            employee.save()
            return HttpResponse("<h2>Data is saved in the database.</h2>")
    return render(request, 'app01/employeeForm.html', {"form":form})
