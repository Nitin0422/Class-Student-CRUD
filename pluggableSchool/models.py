from django.db import models

# Create your models here.
class Class(models.Model):
    class_name = models.CharField(max_length=200)
    block = models.CharField(max_length=200)

class Student(models.Model):
    classroom = models.ForeignKey(Class, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)