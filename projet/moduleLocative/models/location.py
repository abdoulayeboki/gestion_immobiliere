from django.db import models
from moduleAdministrative.models.bienImmobilier import BienImmobilier

from moduleLocative.models.locataire import Locataire

from .enumeration import   JourEcheace
#  fonction pour importer une image
def upload_path(instance, filename):
    return '/'.join(['media',str(instance.numero), filename])

class Location(models.Model):
    numero = models.CharField(max_length=20, unique=True,blank=True)
    loyer = models.FloatField()
    charge = models.FloatField() 
    montantCommission = models.FloatField()         
    debutBail = models.DateField()
    finBail = models.DateField()
    pourcentageTaxe = models.FloatField()
    soldeAnterieur = models.FloatField(default=0)
    cretedDate = models.DateTimeField(auto_now_add=True)
    contratBail = models.FileField(blank=True,null=True, upload_to=upload_path)
    jourEcheace = models.CharField(max_length=15,choices= [(j.value, j.value) for j in JourEcheace],default="semaine_1") 
    locataire = models.ForeignKey(Locataire,on_delete=models.CASCADE,related_name="locations")
    bienImmobilier = models.ForeignKey(BienImmobilier,on_delete=models.CASCADE,related_name="locations")
    
    class Meta:
        pass
        # unique_together = [['cni'],['user']]
        
    def __str__(self):
        return self.numero
    def save(self, *args, **kwargs):
        if not self.numero:
            if  Location.objects.count() !=0: #si la table est vide
                last = Location.objects.latest('id')
                numero = "LOCATION_"+"%06d" % (last.id+1,)
            else:
                numero = "LOCATION__"+"%06d" % (1,)
            self.numero = numero
        super().save(*args, **kwargs) 
    @property
    def  loyerTotal(self):
        return self.ttc + self.charge
    @property
    def tva(self):
        return (self.loyer * self.pourcentageTaxe)/100
    @property
    def ttc(self):
        return self.tva + self.loyer
    def clean(self):
        pass
        # from django.core.exceptions import ValidationError
        # if self.chargeMensuel > self.prixMensuel:
        #     raise ValidationError('la charge mensuelle ne devrait pas etre supérieur au prix mensuel')
        # if self.prixMensuel <10000:
        #     raise ValidationError('le prix doit etre supérieur à 10000')
    
