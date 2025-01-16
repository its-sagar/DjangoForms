from django.db import models

# Create your models here.

class Employee(models.Model):
    Name = models.CharField(max_length=200, null=False, blank=False)
    Salary = models.IntegerField()

