from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def employee(request):
    return render(request, 'employee.html')