# from django.db import models
from django.contrib.gis.db import models
from django.contrib.gis.geos import Point 



# Create your models here.
class Parcelle(models.Model):
   num_parcelle = models.CharField(max_length=100, unique=True)
   usage = models.CharField(max_length=100)
   superficie = models.FloatField()
   proprietaire = models.CharField(max_length=255)
   contact = models.CharField(max_length=255)
   geom = models.PolygonField(srid=4326)



def __str__(self):
        return self.num_parcelle