from rest_framework import serializers
from ..models.immeuble import Immeuble
class ImmeubleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Immeuble
        exclude =[]
        # fields = ['numero','nomBien','prixMensuel','chargeMensuel']