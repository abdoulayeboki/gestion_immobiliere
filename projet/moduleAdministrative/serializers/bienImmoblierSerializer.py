from rest_framework import serializers
from ..models.bienImmobilier import BienImmobilier
class BienImmoblierSerializer(serializers.ModelSerializer):
    class Meta:
        model =BienImmobilier
        fields = "__all__"