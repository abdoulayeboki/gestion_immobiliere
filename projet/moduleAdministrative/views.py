from django.shortcuts import render
from rest_framework import generics

from .serializers.maisonSerializer import MaisonSerializer

from .models.maison import Maison
from .models.appartement import Appartement
from .models.immeuble import Immeuble
from .models.proprietaire import Proprietaire
from .serializers.appartementSerializer import AppartementSerializer
from .serializers.immeubleSerializer import ImmeubleSerializer
from .serializers.proprietaireSerializer import ProprietaireSerializer
# Create your views here.
# view Departement   
class AppartementList(generics.ListAPIView):
    queryset = Appartement.objects.all()
    serializer_class = AppartementSerializer
    # filter_backends = [filters.SearchFilter]
    # search_fields = ['nom','code']
class AppartementOne(generics.RetrieveAPIView): # new
    queryset = Appartement.objects.all()
    serializer_class = AppartementSerializer  
class MaisonList(generics.ListAPIView):
    queryset = Maison.objects.all()
    serializer_class = MaisonSerializer
class MaisonOne(generics.RetrieveAPIView): # new
    queryset = Maison.objects.all()
    serializer_class = MaisonSerializer 
class ImmeubleList(generics.ListAPIView):
    queryset = Immeuble.objects.all()
    serializer_class = ImmeubleSerializer
class ImmeubleOne(generics.RetrieveAPIView): # new
    queryset = Immeuble.objects.all()
    serializer_class = ImmeubleSerializer    
class ProprietaireList(generics.ListAPIView):
    queryset = Proprietaire.objects.all()
    serializer_class = ProprietaireSerializer
class ProprietaireOne(generics.RetrieveAPIView): # new
    queryset = Proprietaire.objects.all()
    serializer_class = ProprietaireSerializer