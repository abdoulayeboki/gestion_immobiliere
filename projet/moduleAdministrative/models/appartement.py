from django.db import models

from  ..service import calculNumero

from .immeuble import Immeuble
from  .bienImmobilier import BienImmobilier
from .enumeration import Niveau, TypeAppartement

class Appartement(BienImmobilier):
    typeAppartement = models.CharField(max_length=6,choices= [(t.value, t.value) for t in TypeAppartement])
    niveau = models.CharField(max_length=10,choices= [(n.value, n.value) for n in Niveau])
    immeuble = models.ForeignKey(Immeuble,on_delete=models.CASCADE)
    
    
    class Meta:
        pass
        # unique_together = [['cni'],['user']]
        
    def __str__(self):
        return self.typeAppartement
    def save(self, *args, **kwargs):
        self.adresse = self.immeuble.adresse
        self.zone = self.immeuble.zone
        self.proprietaire = self.immeuble.proprietaire
        self.etat = self.immeuble.etat
        self.numero =  calculNumero("578")
        super().save(*args, **kwargs) 