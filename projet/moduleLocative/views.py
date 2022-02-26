from rest_framework import generics

from .serializers.locationSerializer import EtatDesLieuxSerializer, LocataireSerializer, LocationSerializer

from .models.location import Location
from .models.locataire import Locataire
from .models.etatDesLieux import EtatDesLieux

# locatire serializer
class LocataireList(generics.ListCreateAPIView):
    queryset = Locataire.objects.all()
    serializer_class = LocataireSerializer
    # filter_backends = [filters.SearchFilter]
    # search_fields = ['nom','code']
class LocataireDetail(generics.RetrieveUpdateAPIView): # new
    queryset = Locataire.objects.all()
    serializer_class = LocataireSerializer  

# location serializer
class LocationList(generics.ListCreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
class LocationDetail(generics.RetrieveUpdateAPIView): # new
    queryset = Location.objects.all()
    serializer_class = LocationSerializer 
    
# etatdeslieux serializer
class EtatDesLieuxList(generics.ListCreateAPIView):
    queryset = EtatDesLieux.objects.all()
    serializer_class = EtatDesLieuxSerializer
class EtatDesLieuxDetail(generics.RetrieveUpdateAPIView): # new
    queryset = EtatDesLieux.objects.all()
    serializer_class = EtatDesLieuxSerializer