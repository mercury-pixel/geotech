from django.contrib import admin
from .models import Parcelle
from leaflet.admin import LeafletGeoAdmin

# Register your models here.

@admin.register(Parcelle)
class ParcelleAdmin(LeafletGeoAdmin):
    list_display = ('num_parcelle', 'usage', 'superficie', 'proprietaire', 'contact')
    search_fields = ('num_parcelle', 'proprietaire')
    list_filter = ('usage',)

    6.82816, -5.26480