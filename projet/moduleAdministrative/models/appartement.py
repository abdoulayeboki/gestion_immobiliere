from django.db import IntegrityError, models

from moduleLocative.models.enumeration import Lettre


from .immeuble import Immeuble
from  .bienImmobilier import BienImmobilier
from .enumeration import Niveau, TypeAppartement
from django.core.exceptions import ValidationError,FieldError

# 
class Appartement(BienImmobilier):
    typeAppartement = models.CharField(max_length=6,choices= [(t.value, t.value) for t in TypeAppartement])
    niveau = models.CharField(max_length=50,choices= [(n.value, n.value) for n in Niveau])
    immeuble = models.ForeignKey(Immeuble,on_delete=models.CASCADE)
    lettre = models.CharField(max_length=1,choices= [(l.value, l.value) for l in Lettre])
    
    class Meta:
        pass
        # unique_together = ['lettre','niveau']
        
    def __str__(self):
        return self.reference
    def save(self, *args, **kwargs):
        self.adresse = self.immeuble.adresse
        self.zone = self.immeuble.zone
        self.proprietaire = self.immeuble.proprietaire
        self.etat = self.immeuble.etat
        self.reference =self.lettre +'-' + self.immeuble.reference  #on recupere la reference de l'immeuble
        print()
        if not self.numero:
            
            if  Appartement.objects.count() !=0: #si la table est vide
                last = Appartement.objects.latest('id')
                numero = "APP-"+"%03d" % (last.id+1,)
            else:
                numero = "APP-"+"%03d" % (1,)
            self.numero = numero
        super().save(*args, **kwargs) 
    # def clean(self):
       
    #     if verifie(self.immeuble.categorie,self.niveau):
    #         raise ValidationError('erreur sur le niveau')

#def verifie (categorie,niveau):
    #         print(niveau not in ("etage_0",))
#         if categorie =='RO':
#             if niveau not in ("etage_0",):
#                 return True
#         if categorie =='R1':
#             if niveau not in ("etage_0","etage_1"):
#                 return True
#         if categorie =='R2':
#             if niveau not in ("etage_0","etage_1","etage_2"):
#                 return True
#         if categorie =='R3':
#             if niveau not in ("etage_0","etage_1","etage_2","etage_3"):
#                 return True
#         if categorie =='R4':
#             if niveau not in ("etage_0","etage_1","etage_2","etage_3","etage_4"):
#                 return True
#         if categorie =='R5':
#             if niveau not in ("etage_0","etage_1","etage_2","etage_3","etage_4","etage_5"):
#                 return True
#         if categorie =='R6':
#             if niveau not in ("etage_0","etage_1","etage_3","etage_4","etage_5","etage_6"):
#                 return True
#         if categorie =='R7':
#             if niveau not in ("etage_0","etage_1","etage_3","etage_4","etage_5","etage_6","etage_7"):
#                 return True
#         if categorie =='R8':
#             if niveau not in ("etage_0","etage_1","etage_2","etage_3","etage_4","etage_5","etage_6","etage_7","etage_8"):
#                 return True
#         if categorie =='R9':
#             if niveau not in ("etage_0","etage_1","etage_3","etage_4","etage_5","etage_6","etage_7","etage_8","etage_9"):
#                 return True
#         if categorie =='R10':
#             if niveau not in ("etage_0","etage_1","etage_3","etage_4","etage_5","etage_6","etage_7","etage_8","etage_9","etage_10"):
#                 return Tru