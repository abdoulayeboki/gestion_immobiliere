from django.db import models

from .enumeration import Categorie
class Immeuble(models.Model):
    numero = models.CharField(max_length=20, unique=True)
    nomImmeuble = models.CharField(max_length=20)
    description = models.TextField()
    photo = models.CharField(max_length=250)
    adresse = models.CharField(max_length=200)
    categorie = models.CharField(max_length=3,choices= [(cat.value, cat.value) for cat in Categorie],default='R0')

    class Meta:
        pass
        # unique_together = [['cni'],['user']]
        
    def __str__(self):
        return self.numero
    # def save(self, *args, **kwargs):
    #     # self.profil = 'AUTRE'
    #     super().save(*args, **kwargs)