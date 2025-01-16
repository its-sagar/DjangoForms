from django.db import models

# Create your models here.

class Employee(models.Model):
    Name = models.CharField(max_length=50)
    Salary = models.IntegerField()
    Score = models.FloatField()
    EmpJoiningDate = models.DateField()
    is_employee = models.BooleanField()
    