from django.urls import path
from . import views

urlpatterns = [
    path("app02/employee/", views.employeeData, name="employee02")
]