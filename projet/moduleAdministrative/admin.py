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
            'fields': (('nom', 'prenom'),('telephon','email'),('adresse'))
        }),
    )
     list_display   = ('numero','nom', 'prenom','telephon','email')
     search_fields  = ('numero', 'nom', 'prenom')
class AppartementAdmin(admin.ModelAdmin):
     exclude = ('zone','etat','adresse','numero')
     list_display   = ('numero','etat','adresse')
     list_filter    = ('immeuble__numero',)
     search_fields  = ('numero',)
class ImmeubleAdmin(admin.ModelAdmin):
     exclude = ('numero',)
     list_display   = ('numero', 'nomImmeuble', 'proprietaire')
     list_filter    = ('proprietaire__numero',)
     search_fields  = ('numero', 'nomImmeuble')
     fieldsets = (
        ("Information Personnelle", {
            'fields': (('nomImmeuble', 'photo',),('etat','categorie','proprietaire'),('adresse','zone',),('description'))
        }),
    )
class MaisonAdmin(admin.ModelAdmin):
     exclude = ('numero',)
     list_display   = ('numero', 'proprietaire')
     list_filter    = ('proprietaire__numero',)
     search_fields  = ('numero', 'nomBien')
     fieldsets = (
        ("Information Personnelle", {
            'fields': (('etat','zone',),('nbrPiece','proprietaire'),'typePiece',)
        }),
    )
# class FiliereAdmin(admin.ModelAdmin):
#      exclude = ('code',)
#      list_display   = ('code', 'nom', 'departement')
#      list_filter    = ('departement',)
#      search_fields  = ('code', 'nom')



admin.site.register(Zone)
# admin.site.register(BienImmobilier)
admin.site.register(Appartement,AppartementAdmin)
admin.site.register(Immeuble,ImmeubleAdmin)
admin.site.register(Maison,MaisonAdmin)
admin.site.register(Proprietaire,ProprietaireAdmin)