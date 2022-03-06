from rest_framework import serializers
from ..models.immeuble import Immeuble
from .proprietaireSerializer import ProprietaireSerializer

class ImmeubleSerializer(serializers.ModelSerializer):
    proprietaire =  ProprietaireSerializer(read_only=True)
    class Meta:
        model = Immeuble
        exclude =[]
        # fields = ['numero','nomBien','prixMensuel','chargeMensuel']