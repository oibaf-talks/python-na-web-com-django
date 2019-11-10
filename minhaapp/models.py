from django.db import models

# Create your models here.

class Presenca(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(null=False, blank=False, max_length=100)
    date = models.DateField(null=False, blank=False, auto_now=False, auto_now_add=False)
