from django.db import models

# Create your models here.

class Department(models.Model):
    department = models.CharField(max_length=50)
    faculty = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.department
        
class Student(models.Model):
    name = models.CharField(max_length = 50)
    birth_date = models.DateField()
    location = models.CharField(max_length = 50)

    def __str__(self) -> str:
        return self.name