from django.db import models

# Create your models here.
class Colonne(models.Model):
    pos_col = models.IntegerField(null=False)
    nom_col = models.CharField(max_length=100)

class Tache(models.Model):
    pos_task = models.IntegerField(null=False)
    nom_task = models.CharField(max_length=100)