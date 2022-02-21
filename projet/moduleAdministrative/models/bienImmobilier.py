from django.db import models

from .enumeration import  EtatBien
class BienImmobilier(models.Model):
    numero = models.CharField(max_length=20, unique=True)
    nomBien = models.CharField(max_length=20)
    description = models.TextField()
    prixMensuel = models.FloatField()
    chargeMensuel = models.FloatField()
    statut = models.BooleanField(default=False)
    photo = models.CharField(max_length=250)
    adresse = models.CharField(max_length=200)
    etat = models.CharField(max_length=15,choices= [(etat.value, etat.value) for etat in EtatBien])
    
    class Meta:
        pass
        # unique_together = [['cni'],['user']]
        
    def __str__(self):
        return self.numero
    # def save(self, *args, **kwargs):
    #     # self.profil = 'AUTRE'
    #     super().save(*args, **kwargs) 