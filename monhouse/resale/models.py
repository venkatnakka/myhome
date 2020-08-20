from django.db import models


# Create your models here.
class PropertyDetail(models.Model):
    apartmenttype = models.CharField(max_length=20,blank=False)
    apartmentname = models.CharField(max_length=20,blank=False)
    ownershiptype = models.CharField(max_length=20)
    propertyage   = models.CharField(max_length=50)
    bhktype       = models.CharField(max_length=20,blank=False)
    floor         = models.IntegerField(blank=False)
    totalfloor    = models.IntegerField(blank=False)
    floortype     = models.CharField(max_length=30)
    no_of_units   = models.IntegerField()
    facing        = models.CharField(max_length=20,blank=True)
    propertysize  = models.IntegerField(blank=False)

    def __str__(self):
        return self.apartmenttype

class LocationDetail(models.Model):
    city     = models.CharField(max_length=50,blank=False)
    locality = models.CharField(max_length=150,blank=False)
    street   = models.CharField(max_length=150,blank=False)

    def __str__(self):
        return self.city

class Resaledetail(models.Model):
    expectedprice   = models.CharField(max_length=20,blank=False)
    maintenancecost = models.CharField(max_length=20,blank=False)
    possessiondate  = models.DateTimeField()
    kitchen_type    = models.CharField(max_length=50)
    furnishing      = models.CharField(max_length=20,blank=False)
    parking         = models.CharField(max_length=30)


class Imagedetail(models.Model):
    image= models.CharField(max_length=20,blank=True)


    def __str__(self):
        return self.image

class Amenities(models.Model):
    bathroom           = models.IntegerField()
    balcony            = models.IntegerField()
    watersupply        = models.CharField(max_length=20)
    gym                = models.BooleanField(default=True)
    nonvegallowed      = models.BooleanField(default=True)
    showinghouse       = models.CharField(max_length=20)
    secondarynumber    = models.IntegerField()
    amenitiesavailable = models.CharField(max_length=400)
    

class AdditionalInformation(models.Model):
    saleDeedCertificate  = models.BooleanField(default=True)
    propertytax          = models.BooleanField(default=True)
    occupancyCertificate = models.BooleanField(default=True)

class Schedule(models.Model):
    availabilty       = models.CharField(max_length=30)
    startTime         = models.DateTimeField()
    endTime           = models.DateTimeField()
    availabiltyAllDay = models.BooleanField(default=False)
