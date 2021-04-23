from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=20)
    contact = models.CharField(max_length=20)

    def __str__(self):
       return self.name

class Employee(models.Model):
    name = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    contact = models.CharField(max_length=20)
    departments = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


# Create your models here.
