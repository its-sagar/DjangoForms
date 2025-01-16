from django.shortcuts import render
from django.http import HttpResponse
from .forms import EmployeeForm
from .models import Employee



# Create your views here.

def employeeData(request):
    form =  EmployeeForm()
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['Name']
            salary = form.cleaned_data['Salary']
            score = form.cleaned_data['Score']
            is_employee = form.cleaned_data['is_employee']

            employee = Employee.objects.create(
                Name = name,
                Salary = salary,
                Score = score,
                is_employee = is_employee
            )

            employee.save()
            return HttpResponse("Data Saved Successfully.")
    return render(request, 'app03/employeeForm.html', {"form":form})