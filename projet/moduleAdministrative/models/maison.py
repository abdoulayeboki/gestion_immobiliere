from django.db import models
from .bienImmobilier import BienImmobilier

class Maison(BienImmobilier):
    nbrPiece = models.IntegerField()
    typePiece = models.CharField(max_length=200)
    jardin = models.BooleanField(default=False)

    class Meta:
        pass
        # unique_together = [['cni'],['user']]
        
    def __str__(self):
        return self.typePiece
    # def save(self, *args, **kwargs):
    #     # self.profil = 'AUTRE'
    #     super().save(*args, **kwargs)