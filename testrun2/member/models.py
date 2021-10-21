from django.db import models

# Create your models here.
class Person (models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=255)
    DoB = models.DateField()
    contact = models.IntegerField()

    def __str__(self) -> str:
        return self.name