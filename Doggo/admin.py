from django.contrib import admin

# Register your models here.
from .models import Kandydat, Partia, Wybory

admin.site.register(Partia)
admin.site.register(Wybory)
admin.site.register(Kandydat)
