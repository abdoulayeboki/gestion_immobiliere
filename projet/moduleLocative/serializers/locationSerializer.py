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
    locataire =  LocataireSerializer(read_only=True)
    bienImmobilier =  BienImmoblierSerializer(read_only=True)
    class Meta:
        model = Location
        fields = "__all__"
class LocationPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = "__all__"
class EtatDesLieuxSerializer(serializers.ModelSerializer):
    class Meta:
        model = EtatDesLieux
        # exclude =[]
        fields = "__all__"