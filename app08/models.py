from django.db import models

# Create your models here.

class Employee(models.Model):
    Name = models.CharField(max_length=50)
    profile_img = models.ImageField(null=True, blank=True, upload_to="media/")
