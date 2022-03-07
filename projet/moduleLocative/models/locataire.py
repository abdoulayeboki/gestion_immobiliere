from django.db import models

class Locataire(models.Model):
    nom = models.CharField(max_length=20)
    prenom = models.CharField(max_length=100)
    numero = models.CharField(max_length=20, unique=True)
    telephon = models.CharField(max_length=18)
    email = models.CharField(max_length=100,default="")
    adresse = models.CharField(max_length=200,default="")

    class Meta:
        pass
        # unique_together = [['cni'],['user']]
        
    def __str__(self):
        return self.prenom
    def save(self, *args, **kwargs):
        if not self.numero:
            if  Locataire.objects.count() !=0: #si la table est vide
                last = Locataire.objects.latest('id')
                numero = "LCT-"+"%06d" % (last.id+1,)
            else:
                numero = "LCT-"+"%06d" % (1,)
            self.numero = numero
        super().save(*args, **kwargs)