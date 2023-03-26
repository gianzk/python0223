from django.db import models

# Create your models here.


class Proyect(models.Model):
    titulo=models.CharField(max_length=200)
    description=models.TextField()