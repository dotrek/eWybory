from django.contrib import admin

# Register your models here.
from .models import Kandydat, Partia, Wybory, Glos, Glosujacy

admin.site.register(Partia)
admin.site.register(Wybory)
admin.site.register(Kandydat)
admin.site.register(Glos)
admin.site.register(Glosujacy)
