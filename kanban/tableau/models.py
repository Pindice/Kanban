from django.db import models

# Create your models here.
class Colonne(models.Model):
    pos_col = models.IntegerField(null=False)
    nom_col = models.CharField(max_length=100)

    def __str__(self):
        return self.nom_col

class Tache(models.Model):
    pos_task = models.IntegerField(null=False)
    nom_task = models.CharField(max_length=100)
    col_task = models.ForeignKey(Colonne, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom_task