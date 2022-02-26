from django.contrib import admin

from .models.etatDesLieux import EtatDesLieux

from .models.locataire import Locataire
from .models.location import Location

class LocataireAdmin(admin.ModelAdmin):
     exclude = ('numero',)
     fieldsets = (
        ("Information Personnelle", {
            'fields': ('nom', 'prenom','telephon','email','adresse')
        }),
    )
     list_display   = ('numero','nom', 'prenom','telephon','email')
     search_fields  = ('numero', 'nom', 'prenom','telephon',)



admin.site.register(Locataire,LocataireAdmin)
admin.site.register(Location)
admin.site.register(EtatDesLieux)