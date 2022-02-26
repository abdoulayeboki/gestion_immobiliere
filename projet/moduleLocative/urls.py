from django.urls import path

from .views import  LocationList, LocationDetail, LocataireList, LocataireDetail, EtatDesLieuxList, EtatDesLieuxDetail


urlpatterns = [
    path('locations/', LocationList.as_view(), name='location_list'),
    path('etat_des_lieux/', EtatDesLieuxList.as_view(), name='etat_des_lieux_list'),
    path('locataires/', LocataireList.as_view(), name='locataire_list'),
    path('locations/<int:pk>/', LocationDetail.as_view(), name='location_detail'),
    path('etat_des_lieux/<int:pk>/', EtatDesLieuxDetail.as_view(), name='eetat_des_lieux_detail'),
    path('locataires/<int:pk>/', LocataireDetail.as_view(), name='locataire_detail'),
    
]
