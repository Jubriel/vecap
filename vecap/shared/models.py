from django.db import models

# Create your models here.
class Faith(models.Model):
    bornagain = models.BooleanField()
    #denomination = models.CharField(max_length=50)
