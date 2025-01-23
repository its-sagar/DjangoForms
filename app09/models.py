from django.db import models

# Create your models here.

class Employee(models.Model):
    gender_choice = [
        ("Male","Male"),
        ("Female","Female"),
        ("Other","Other")
    ]
    Name = models.CharField(max_length=50)
    Salary = models.IntegerField()
    Gender = models.CharField(
        choices=gender_choice,
        null=True,
        blank=True,
        max_length=50
    )
