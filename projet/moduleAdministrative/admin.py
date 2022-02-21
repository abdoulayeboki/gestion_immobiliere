from django.contrib import admin

# from .models.bienImmobilier import BienImmobilier
from .models.proprietaire import Proprietaire
from .models.zone import Zone

from .models.appartement import Appartement
from .models.immeuble import Immeuble
from .models.maison import Maison

# Register your models here.
admin.site.register(Zone)
# admin.site.register(BienImmobilier)
admin.site.register(Appartement)
admin.site.register(Immeuble)
admin.site.register(Maison)
admin.site.register(Proprietaire)