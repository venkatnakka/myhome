from django.db import models


# Create your models here.
class PropertyDetail(models.Model):
    apartmenttype = models.CharField(max_length=20,blank=False)
    apertmentname = models.CharField(max_length=40,blank=False)
    bhktype       = models.CharField(max_length=20,blank=False)
    floor         = models.IntegerField(blank=False)
    totalfloor    = models.IntegerField(blank=False)
    # facing        = models.CharField(max_length=20,blank=True)
    propertysize  = models.IntegerField(blank=False)

    def __str__(self):
        return self.apartmenttype
        abstract = True

class LocationDetail(models.Model):
    city = models.CharField(max_length=50,blank=False)
    locality= models.CharField(max_length=150,blank=False)
    # street = models.CharField(max_length=150,blank=False)

    def __str__(self):
        return self.city
        abstract = True