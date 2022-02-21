from django.db import models

from  .bienImmobilier import BienImmobilier
from .enumeration import Niveau, TypeAppartement

class Appartement(BienImmobilier):
    typeAppartement = models.CharField(max_length=6,choices= [(t.value, t.value) for t in TypeAppartement])
    niveau = models.CharField(max_length=10,choices= [(n.value, n.value) for n in Niveau])
    
    
    class Meta:
        pass
        # unique_together = [['cni'],['user']]
        
    def __str__(self):
        return self.typeAppartement
    # def save(self, *args, **kwargs):
    #     # self.profil = 'AUTRE'
    #     super().save(*args, **kwargs) 
