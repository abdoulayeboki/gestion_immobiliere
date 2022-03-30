from rest_framework import generics

from .serializers.locationSerializer import EtatDesLieuxSerializer, LocataireSerializer, LocationPostSerializer, LocationSerializer

from .models.location import Location
from .models.locataire import Locataire
from .models.etatDesLieux import EtatDesLieux

# locatire serializer
class LocataireList(generics.ListCreateAPIView):
    queryset = Locataire.objects.all()
    serializer_class = LocataireSerializer
    # filter_backends = [filters.SearchFilter]
    # search_fields = ['nom','code']
class LocataireDetail(generics.RetrieveUpdateDestroyAPIView): # new
    queryset = Locataire.objects.all()
    serializer_class = LocataireSerializer  

# location view
class LocationList(generics.ListCreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer 
class LocationCreate(generics.CreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationPostSerializer
     
class LocationDetail(generics.RetrieveUpdateDestroyAPIView): # new
    queryset = Location.objects.all()
    serializer_class = LocationSerializer     
# etatdeslieux view
class EtatDesLieuxList(generics.ListCreateAPIView):
    queryset = EtatDesLieux.objects.all()
    serializer_class = EtatDesLieuxSerializer
class EtatDesLieuxDetail(generics.RetrieveUpdateAPIView): # new
    queryset = EtatDesLieux.objects.all()
    serializer_class = EtatDesLieuxSerializer