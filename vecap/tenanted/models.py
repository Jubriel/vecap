from shared.models import Faith
from django.db import models

# Create your models here.
class Member(models.Model):
    name = models.CharField(max_length=100)
    bornagain = models.ForeignKey(Faith, on_delete=models.CASCADE)
    #denominaton = models.ForeignKey(Faith, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name