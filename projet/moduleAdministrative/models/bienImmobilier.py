from django.db import models
from .zone import Zone
from .proprietaire import Proprietaire
from .enumeration import  EtatBien
class BienImmobilier(models.Model):
    numero = models.CharField(max_length=20, unique=True)
    # nomBien = models.CharField(max_length=20)    
    # prixMensuel = models.FloatField()
    # chargeMensuel = models.FloatField()
    # statut = models.BooleanField(default=False)
    # photo = models.CharField(max_length=250)
    adresse = models.CharField(max_length=200,null=True)
    etat = models.CharField(max_length=15,choices= [(etat.value, etat.value) for etat in EtatBien])
    zone = models.ForeignKey(Zone,on_delete=models.DO_NOTHING,default=None)
    proprietaire = models.ForeignKey(Proprietaire,on_delete=models.DO_NOTHING,default=None)
    # description = models.TextField()
    class Meta:
        pass
        # unique_together = [['cni'],['user']]
        
    def __str__(self):
        return self.numero
    # def save(self, *args, **kwargs):
    #     # self.profil = 'AUTRE'
    #     super().save(*args, **kwargs) 