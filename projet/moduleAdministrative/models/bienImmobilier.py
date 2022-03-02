from django.db import models
from .zone import Zone
from .proprietaire import Proprietaire
from .enumeration import  EtatBien

#  fonction pour importer une image
def upload_path(instance, filename):
    return '/'.join(['media',str(instance.numero), filename])

class BienImmobilier(models.Model):
    numero = models.CharField(max_length=20, unique=True)
    reference = models.CharField(max_length=100, unique=True)    
    statut = models.BooleanField(default=False)
    photo = models.ImageField(blank=True,null=True, upload_to=upload_path) 
    adresse = models.CharField(max_length=200)
    etat = models.CharField(max_length=15,choices= [(etat.value, etat.value) for etat in EtatBien],default="neuf")
    zone = models.ForeignKey(Zone,on_delete=models.DO_NOTHING)
    proprietaire = models.ForeignKey(Proprietaire,on_delete=models.DO_NOTHING)
    description = models.TextField(blank=True,null=True)
    class Meta:
        pass
        # unique_together = [['cni'],['user']]
        
    def __str__(self):
        return self.reference
    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs) 
    # def clean(self):
    #     from django.core.exceptions import ValidationError
    #     if self.chargeMensuel > self.prixMensuel:
    #         raise ValidationError('la charge mensuelle ne devrait pas etre supérieur au prix mensuel')
    #     if self.prixMensuel <10000:
    #         raise ValidationError('le prix doit etre supérieur à 10000')
    
