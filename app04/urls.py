from django.urls import path
from . import views

urlpatterns = [
    path('app04/employee/', views.employeeData, name="employee04")
]