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
    class Meta:
        abstract = True

class LocationDetail(models.Model):
    city = models.CharField(max_length=50,blank=False,null=True)
    locality= models.CharField(max_length=150,blank=False)
    # street = models.CharField(max_length=150,blank=False)

    def __str__(self):
        return self.city
    class Meta:
        abstract = True

class Schedule(models.Model):
    availabilty       = models.CharField(max_length=30)
    startTime         = models.DateTimeField()
    endTime           = models.DateTimeField()
    availabiltyAllDay = models.BooleanField(default=False)

    def __str__(self):
        return self.availabilty
    class Meta:
        abstract = True

class Amenities(models.Model):

    bathroom = models.IntegerField()
    balcony = models.IntegerField()
    watersupply=models.CharField(max_length=20)
    gym = models.BooleanField(default=False)
    nonvegallowed = models.BooleanField(default=True)
    showinghouse = models.CharField(max_length=20)
    secondarynumber = models.IntegerField()
    amenitiesavailable=models.CharField(max_length=400)

    class Meta:
        abstract = True
