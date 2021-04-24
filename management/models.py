from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=20)
    empid = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    def __str__(self):
        return self.name

class Project(models.Model):
    name = models.CharField(max_length=20)
    ptype = models.CharField(max_length=20)
    def __str__(self):
        return self.name

# Create your models here.
