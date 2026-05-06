from django.urls import path
from .views import ParcelleGeoAPIView, carte_cadastral


urlpatterns = [
    path('api/parcelles/', ParcelleGeoAPIView.as_view(), name='parcelle-geo-api'),
    path('', carte_cadastral, name='carte-cadastral')
]