from django.shortcuts import render
from django.http import HttpResponse
from . models import Employee
from . forms import EmployeeForm

# Create your views here.

def employeeData(request):
    form = EmployeeForm()
    if request.method == "POST":
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['Name'],
            profile_img = form.cleaned_data['profile_img']

            employee = Employee(
                Name = name,
                profile_img  = profile_img
            )
            employee.save()
            return HttpResponse("Data is saved in Database successfully.")
    return render(request, 'app08/employeeForm.html', {"form":form})
