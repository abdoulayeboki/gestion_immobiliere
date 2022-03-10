from rest_framework import filters
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
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.
# view Departement   
class AppartementList(generics.ListAPIView):
    queryset = Appartement.objects.all()
    serializer_class = AppartementSerializer
    filter_backends = [DjangoFilterBackend,filters.SearchFilter]
    search_fields = ['numero','reference']
    filterset_fields = ['numero','reference','statut']
class AppartementOne(generics.RetrieveAPIView): # new
    queryset = Appartement.objects.all()
    serializer_class = AppartementSerializer  
class MaisonList(generics.ListAPIView):
    queryset = Maison.objects.all()
    serializer_class = MaisonSerializer
    filter_backends = [DjangoFilterBackend,filters.SearchFilter]
    filterset_fields = ['numero','reference','statut']
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