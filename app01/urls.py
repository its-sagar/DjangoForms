from django.urls import path
from . import views

urlpatterns = [
    path("app01/employee/", views.employeeData, name="employee01")
]