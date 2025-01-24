from django.db import models

# Create your models here.
class Position(models.Model):
    Position_name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.Position_name


class Employee(models.Model):
    gender = [
        ("Male","Male"),
        ("Female","Female"),
        ("Other","Other"),
    ]
    Name = models.CharField(max_length=50)
    Email = models.EmailField()
    Gender = models.CharField(choices=gender, max_length=50,)
    Position = models.ManyToManyField(Position, blank=True, null=True)
