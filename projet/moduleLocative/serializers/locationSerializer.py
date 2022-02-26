# from moduleAdministrative.serializers.appartementSerializer import AppartementSerializer
from moduleAdministrative.serializers.bienImmoblierSerializer import BienImmoblierSerializer
from ..models.etatDesLieux import EtatDesLieux
from ..models.locataire import Locataire

from rest_framework import serializers
from ..models.location import Location

class LocataireSerializer(serializers.ModelSerializer):
    class Meta:
        model = Locataire
        # exclude =[]
        fields = "__all__"
class LocationSerializer(serializers.ModelSerializer):
    locataire =  LocataireSerializer(write_only=True)
    bienImmobilier =  BienImmoblierSerializer(read_only=True)
    class Meta:
        model = Location
        # exclude =[]
        fields = "__all__"

class EtatDesLieuxSerializer(serializers.ModelSerializer):
    class Meta:
        model = EtatDesLieux
        # exclude =[]
        fields = "__all__"