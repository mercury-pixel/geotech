from rest_framework_gis.serializers import GeoFeatureModelSerializer
from .models import Parcelle

class ParcelleGeoSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Parcelle
        geo_field = 'geom'
        fields = ('num_parcelle', 'usage', 'superficie', 'proprietaire', 'contact')