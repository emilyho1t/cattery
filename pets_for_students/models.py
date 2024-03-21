from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=30, unique=True)
    last_name = models.CharField(max_length=30, unique=True)
    number_of_cats = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Cat(models.Model):
    students = models.ForeignKey(Student, on_delete=models.CASCADE)
    name = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.name
