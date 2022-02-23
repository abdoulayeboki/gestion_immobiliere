from rest_framework import serializers
from ..models.proprietaire import Proprietaire
class ProprietaireSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proprietaire
        exclude =[]
        # fields = ['numero','nomBien','prixMensuel','chargeMensuel']