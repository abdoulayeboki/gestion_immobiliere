from django.db import models

from .zone import Zone
from .proprietaire import Proprietaire
from .enumeration import Categorie, EtatBien
class Immeuble(models.Model):
    numero = models.CharField(max_length=20, unique=True)
    nomImmeuble = models.CharField(max_length=20)
    description = models.TextField()
    photo = models.CharField(max_length=250)
    adresse = models.CharField(max_length=200)
    etat = models.CharField(max_length=15,choices= [(etat.value, etat.value) for etat in EtatBien],default='R0')
    categorie = models.CharField(max_length=3,choices= [(cat.value, cat.value) for cat in Categorie],default='R0')
    zone = models.ForeignKey(Zone,on_delete=models.DO_NOTHING,default=None)
    proprietaire = models.ForeignKey(Proprietaire,on_delete=models.DO_NOTHING,default=None)

    class Meta:
        pass
        # unique_together = [['cni'],['user']]
        
    def __str__(self):
        return self.numero
    def save(self, *args, **kwargs):
        self.numero = self.nomImmeuble
        super().save(*args, **kwargs)