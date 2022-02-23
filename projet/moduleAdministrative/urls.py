from django.urls import path

from .views import  AppartementList, AppartementOne, ImmeubleList, ImmeubleOne, MaisonList, MaisonOne, ProprietaireList, ProprietaireOne


urlpatterns = [
    path('appartements/', AppartementList.as_view(), name='appartement_list'),
    path('maisons/', MaisonList.as_view(), name='maison_list'),
    path('proprietaires/', ProprietaireList.as_view(), name='proprietaire_list'),
    path('immeubles/', ImmeubleList.as_view(), name='immeuble_list'),
    path('appartements/<int:pk>/', AppartementOne.as_view(), name='appartement_list'),
    path('maisons/<int:pk>/', MaisonOne.as_view(), name='maison_list'),
    path('proprietaires/<int:pk>/', ProprietaireOne.as_view(), name='proprietaire_list'),
    path('immeubles/<int:pk>/', ImmeubleOne.as_view(), name='immeuble_list'),
    
]
