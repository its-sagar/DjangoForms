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
            name = form.cleaned_data['Name']
            file = form.cleaned_data['File']

            employee = Employee(
                Name = name,
                File = file
            )

            employee.save()

            return HttpResponse("Data is saved in database successfully.")
    return render(request, 'app07/employeeForm.html', {'form':form})
