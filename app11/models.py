from django.db import models

# Create your models here.

class Employee(models.Model):
    Username = models.CharField(max_length=50, blank=False, null=False)
    Password = models.CharField(max_length=50, null=False, blank=False)