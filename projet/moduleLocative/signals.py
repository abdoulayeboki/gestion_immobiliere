from django.dispatch import receiver
from django.db.models.signals import post_save,pre_save
from moduleAdministrative.models.bienImmobilier import BienImmobilier
from .models.location import Location

@receiver(post_save, sender=Location)
def post_saveLocation(instance,created, **kwargs):
    if created:
        BienImmobilier.objects.filter(pk=instance.bienImmobilier.id).update(statut=True)
        
