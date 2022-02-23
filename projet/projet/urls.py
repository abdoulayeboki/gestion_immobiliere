
from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('bien_immobilier/', include('moduleAdministrative.urls')),
]


# # pour afficher des images
# if settings.DEBUG:
#   urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)