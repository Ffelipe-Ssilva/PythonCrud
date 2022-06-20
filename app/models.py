from django.db import models

# Create your models here.
class Rider(models.Model):
    nome=models.CharField(max_length=50)
    tema=models.CharField(max_length=50)
    ano=models.IntegerField()
    