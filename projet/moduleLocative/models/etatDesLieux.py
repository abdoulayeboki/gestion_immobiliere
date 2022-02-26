from django.db import models

from .location import Location
from .enumeration import  EtatBien


class EtatDesLieux(models.Model):
    element = models.CharField(max_length=100)
    commentaire = models.CharField(max_length=250)    
    location = models.ForeignKey(Location,on_delete=models.CASCADE,related_name="etatDesLieux")
    etat = models.CharField(max_length=15,choices= [(etat.value, etat.value) for etat in EtatBien],default="neuf")
    class Meta:
        pass
        # unique_together = [['cni'],['user']]
        
    def __str__(self):
        return self.element
    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs) 
    def clean(self):
        pass
    
