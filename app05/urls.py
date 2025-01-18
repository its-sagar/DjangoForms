from django.urls import path
from . import views

urlpatterns = [
    path('app05/employee', views.employeeData, name='employee05')
]