from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Employee, Position
from .forms import EmployeeForm
from django.contrib import messages

# Create your views here.

def employeeData(request):
    form = EmployeeForm()
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()

            # Or you can use this method

            # name = form.cleaned_data['Name']
            # email = form.cleaned_data['Email']
            # gender = form.cleaned_data['Gender']
            # positions = form.cleaned_data['Position']

            # employee = Employee(
            #     Name=name,
            #     Email=email,
            #     Gender=gender,
            # )
            # employee.save()
            # employee.Position.set(positions)  # Assign the positions to the employee
            messages.success(request, "Data is saved in the database successfully.")
            return redirect('home')
        
    return render(request, 'app10/employee_form.html', {"form":form})