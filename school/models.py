from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=20)
    rol_no = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    def __str__(self):
        return self.name

class Teacher(models.Model):
    name = models.CharField(max_length=20)
    teacherid = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    def __str__(self):
        return self.name
# Create your models here.
