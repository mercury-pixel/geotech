from django.shortcuts import render
from rest_framework import generics
from .models import Parcelle
from .serializers import ParcelleGeoSerializer


class ParcelleGeoAPIView(generics.ListAPIView):
    queryset = Parcelle.objects.all()
    serializer_class = ParcelleGeoSerializer #(queryset=queryset, many=True)

# Create your views here.

def carte_cadastral(request):
    return render(request, 'cartographie/carte.html')
