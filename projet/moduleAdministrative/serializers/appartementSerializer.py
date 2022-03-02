from rest_framework import serializers

from .immeubleSerializer import ImmeubleSerializer



from .proprietaireSerializer import ProprietaireSerializer
from ..models.appartement import Appartement
class AppartementSerializer(serializers.ModelSerializer):
    proprietaire =  ProprietaireSerializer(read_only=True)
    immeuble =  ImmeubleSerializer(read_only=True)
    class Meta:
        model = Appartement
        exclude =[]
        # fields = ['numero','reference','prixMensuel','chargeMensuel']