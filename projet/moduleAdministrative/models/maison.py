from django.db import models
from .bienImmobilier import BienImmobilier
from django.core.exceptions import ValidationError
class Maison(BienImmobilier):
    nbrPiece = models.IntegerField()
    typePiece = models.CharField(max_length=250)
    jardin = models.BooleanField(default=False)

    class Meta:
        pass
        # unique_together = [['cni'],['user']]
        
    def __str__(self):
        return self.typePiece
    def save(self, *args, **kwargs):
        if not self.numero:
            lastMaison = Maison.objects.latest('id')
            numero = "M_"+"%06d" % (lastMaison.id+1,)
            self.numero = numero
        super().save(*args, **kwargs)
    def clean(self):
        if self.nbrPiece >= 20:
            raise ValidationError('erreur! le nombre de piece est supérieur à 20')