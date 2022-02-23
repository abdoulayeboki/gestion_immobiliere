from rest_framework import serializers

from .immeubleSerializer import ImmeubleSerializer



from .proprietaireSerializer import ProprietaireSerializer
from ..models.maison import Maison
class MaisonSerializer(serializers.ModelSerializer):
    proprietaire =  ProprietaireSerializer(read_only=True)
    class Meta:
        model = Maison
        exclude =[]
        # fields = ['numero','nomBien','prixMensuel','chargeMensuel']