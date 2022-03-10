from django.dispatch import receiver
from django.db.models.signals import post_save,pre_save,pre_delete
from moduleAdministrative.models.bienImmobilier import BienImmobilier
from .models.location import Location
from django.core.exceptions import PermissionDenied

@receiver(post_save, sender=Location)
def post_saveLocation(instance,created, **kwargs):
    if created:
        BienImmobilier.objects.filter(pk=instance.bienImmobilier.id).update(statut=True)
@receiver(pre_delete, sender=Location)
def pre_deleteLocation(instance, **kwargs):
    BienImmobilier.objects.filter(pk=instance.bienImmobilier.id).update(statut=False)
@receiver(pre_save, sender=Location)
def pre_sevedLocation(instance, **kwargs):
    if instance.debutBail >= instance.finBail:
        raise PermissionDenied('impossible la date  du bail est incorrecte')
    BienImmobilier.objects.filter(pk=instance.bienImmobilier.id).update(statut=False)
       
