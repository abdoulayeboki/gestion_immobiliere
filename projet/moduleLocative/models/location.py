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
    chargeMensuelle = models.FloatField(default=0)
    chargeAjoute= models.FloatField(default=0) 
    montantDepart = models.FloatField(default=0)
    fraisCommission = models.FloatField(default=0)         
    debutBail = models.DateField()
    finBail = models.DateField(default="")
    pourcentageTaxe = models.FloatField(default=0)
    pourcentageCommission = models.FloatField(default=5)
    soldeAnterieur = models.FloatField(default=0)
    createdDate = models.DateTimeField(auto_now_add=True)
    contratBail = models.FileField(blank=True,null=True, upload_to=upload_path)
    jourEcheance = models.CharField(max_length=15,choices= [(j.value, j.value) for j in JourEcheace],default="semaine_1") 
    locataire = models.ForeignKey(Locataire,on_delete=models.CASCADE,related_name="locations")
    bienImmobilier = models.ForeignKey(BienImmobilier,on_delete=models.CASCADE,related_name="locations")
    
    class Meta:
        pass
        # unique_together = [['cni'],['user']]
        
    def __str__(self):
        return self.numero
    def save(self, *args, **kwargs):
        self.fraisCommission = (self.loyer * self.pourcentageCommission)/100
        if not self.numero:
            if  Location.objects.count() !=0: #si la table est vide
                last = Location.objects.latest('id')
                numero = "L-"+"%04d" % (last.id+1,)
            else:
                numero = "L-"+"%04d" % (1,)
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
    
    # @receiver(pre_save, sender=BienImmobilier)
    # def pre_saveLocation(sender, instance,created, **kwargs):
    #     Location.objects.filter(pk=1).update(montantDepart=90000)
    #     print(instance.bienImmobilier.id)
    
 

    def clean(self):
        pass
        # from django.core.exceptions import ValidationError
        # if self.chargeMensuel > self.prixMensuel:
        #     raise ValidationError('la charge mensuelle ne devrait pas etre sup??rieur au prix mensuel')
        # if self.prixMensuel <10000:
        #     raise ValidationError('le prix doit etre sup??rieur ?? 10000')
    
    