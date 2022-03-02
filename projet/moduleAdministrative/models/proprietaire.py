from django.db import models

class Proprietaire(models.Model):
    nom = models.CharField(max_length=20)
    prenom = models.CharField(max_length=100)
    numero = models.CharField(max_length=20, unique=True)
    telephon = models.CharField(max_length=18,default=None)
    email = models.CharField(max_length=100,null=True)
    adresse = models.CharField(max_length=200)

    class Meta:
        pass
        # unique_together = [['cni'],['user']]
        
    def __str__(self):
        return self.prenom
    def save(self, *args, **kwargs):
        if not self.numero:
            if  Proprietaire.objects.count() !=0: #si la table est vide
                last = Proprietaire.objects.latest('id')
                numero = "PRO_"+"%06d" % (last.id+1,)
            else:
                numero = "PRO_"+"%06d" % (1,)
            self.numero = numero
        super().save(*args, **kwargs)