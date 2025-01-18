from django.urls import path
from . import views

urlpatterns = [
    path('app06/employee/', views.employeeData, name='employee06')
]