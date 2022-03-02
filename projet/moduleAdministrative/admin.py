from django.contrib import admin
# from .models.bienImmobilier import BienImmobilier
from .models.proprietaire import Proprietaire
from .models.zone import Zone

from .models.appartement import Appartement
from .models.immeuble import Immeuble
from .models.maison import Maison

# Register your models here.
class ProprietaireAdmin(admin.ModelAdmin):
     exclude = ('numero',)
     fieldsets = (
        ("Information Personnelle", {
            'fields': ('nom', 'prenom','telephon','email','adresse')
        }),
    )
     list_display   = ('numero','nom', 'prenom','telephon','email')
     search_fields  = ('numero', 'nom', 'prenom','telephon',)
class AppartementAdmin(admin.ModelAdmin):
     exclude = ('zone','etat','adresse','numero','proprietaire','reference')
     list_display   = ('numero','reference','immeuble','proprietaire','zone')
     list_filter    = ('immeuble__numero','statut','zone')
     search_fields  = ('numero','reference')
     fieldsets = (
        ("Informations obligatoires", {
            'fields': ('typeAppartement','niveau','immeuble')
        }), 
        ("Informations non obligatoires", {
            'fields': ('photo','description',)
        }),
    )
class ImmeubleAdmin(admin.ModelAdmin):
     exclude = ('numero',)
     list_display   = ('numero', 'reference', 'categorie','proprietaire','zone')
     list_filter    = ('zone','categorie',)
     search_fields  = ('numero', 'reference','categorie',)
     fieldsets = (
        ("Informations obligatoires", {
            'fields': ('reference','zone','categorie','proprietaire','adresse')
        }), 
        ("Informations non obligatoires", {
            'fields': ('etat','photo','description',)
        }),
    )
class MaisonAdmin(admin.ModelAdmin):
     exclude = ('numero',)
     list_display   = ('numero','reference','proprietaire','zone')
     list_filter    = ('proprietaire__numero','statut','zone')
     search_fields  = ('numero', 'reference')
     fieldsets = (
        ("Informations obligatoires", {
            'fields': ('reference','zone','nbrPiece','typePiece','proprietaire')
        }), 
        ("Informations non obligatoires", {
            'fields': ('etat','photo','description',)
        }),
    )

admin.site.register(Zone)
# admin.site.register(BienImmobilier)
admin.site.register(Appartement,AppartementAdmin)
admin.site.register(Immeuble,ImmeubleAdmin)
admin.site.register(Maison,MaisonAdmin)
admin.site.register(Proprietaire,ProprietaireAdmin)
