from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Employee
from .forms import EmployeeForm


# Create your views here.


def employeeData(request):
    form = EmployeeForm()
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['Username']
            password = form.cleaned_data['Password']

            employee = Employee(
                Username=name,
                Password=password
            )

            employee.save()
            messages.success(request, "Data is saved successfully.")
            return redirect('home')
    return render(request, 'app11/employeeForm.html', {"form":form})