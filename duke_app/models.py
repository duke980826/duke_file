from django.db import models

# Create your models here.

class Student(models.Model):
    student_id = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=10)
    grade = models.IntegerField()
    phone = models.CharField(max_length=50)
    amount_due = models.PositiveIntegerField(default=15000)
    def __str__(self):
        return f'{self.student_id} {self.name}'

class Class(models.Model):
    name = models.CharField(max_length=100)
    students = models.ManyToManyField(Student, related_name='classes', blank=True)

    def __str__(self):
        return self.name