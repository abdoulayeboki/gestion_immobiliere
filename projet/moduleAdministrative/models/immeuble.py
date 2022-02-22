from django.db import models

from .zone import Zone
from .proprietaire import Proprietaire
from .enumeration import Categorie, EtatBien

#  fonction pour importer une image
def upload_path(instance, filename):
    return '/'.join(['media',str(instance.numero), filename])
class Immeuble(models.Model):
    numero = models.CharField(max_length=20, unique=True)
    nomImmeuble = models.CharField(max_length=100)
    description = models.TextField(blank=True,null=True,)
    photo = models.ImageField(blank=True,null=True, upload_to=upload_path) 
    adresse = models.CharField(max_length=200)
    etat = models.CharField(max_length=15,choices= [(etat.value, etat.value) for etat in EtatBien],default='neuf')
    categorie = models.CharField(max_length=3,choices= [(cat.value, cat.value) for cat in Categorie],default='R0')
    zone = models.ForeignKey(Zone,on_delete=models.DO_NOTHING)
    proprietaire = models.ForeignKey(Proprietaire,on_delete=models.DO_NOTHING,default=None)

    class Meta:
        pass
        # unique_together = [['cni'],['user']]
        
    def __str__(self):
        return self.numero
    def save(self, *args, **kwargs):
        if not self.numero:
            lastApp = Immeuble.objects.latest('id')
            numero = "IMM_"+"%06d" % (lastApp.id+1,)
            self.numero = numero
        super().save(*args, **kwargs)