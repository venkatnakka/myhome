from django.db import models


# Create your models here.
class PropertyDetail(models.Model):
    apartmenttype = models.CharField(max_length=20,blank=False)
    apartmentname = models.CharField(max_length=20,blank=False)
    bhktype       = models.CharField(max_length=20,blank=False)
    floor         = models.IntegerField(blank=False)
    totalfloor    = models.IntegerField(blank=False)
    facing        = models.CharField(max_length=20,blank=True)
    propertysize  = models.IntegerField(blank=False)

    def __str__(self):
        return self.apartmenttype

class LocationDetail(models.Model):
    city = models.CharField(max_length=50,blank=False)
    locality= models.CharField(max_length=150,blank=False)
    street = models.CharField(max_length=150,blank=False)

    def __str__(self):
        return self.city

class RentalDetail(models.Model):

    availablelease= models.BooleanField(default=True)
    expectedrent= models.IntegerField(blank=False)
    expecteddeposit=models.IntegerField(blank=False)
    maintenance = models.CharField(max_length=30)
    availablefrom = models.DateTimeField(blank=False)
    preferedtenants = models.CharField(max_length=50,blank=False)
    furnishing = models.CharField(max_length=20,blank=False)
    parking = models.CharField(max_length=20,blank=False)


class Imagedetail(models.Model):
    image= models.CharField(max_length=20,blank=True)


    def __str__(self):
        return self.image

class Amenities(models.Model):

    bathroom = models.IntegerField()
    balcony = models.IntegerField()
    watersupply=models.CharField(max_length=20)
    gym = models.BooleanField(default=False)
    nonvegallowed = models.BooleanField(default=True)
    showinghouse = models.CharField(max_length=20)
    secondarynumber = models.IntegerField()
    amenitiesavailable=models.CharField(max_length=400)

