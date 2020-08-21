from django.db import models
from residential.mymodels import *


# Create your models here.
class RentPropertyDetail(PropertyDetail):
    facing        = models.CharField(max_length=20,blank=True)
    datecreated = models.DateTimeField(auto_now_add=True,null=True)


class RentLocationDetail(LocationDetail):
    propertydetails = models.ForeignKey(RentPropertyDetail,on_delete= models.CASCADE)
    street = models.CharField(max_length=150,blank=False)
    


class RentalDetail(models.Model):
    rentallocation = models.ForeignKey(RentLocationDetail,on_delete= models.CASCADE)
    availablelease= models.BooleanField(default=True)
    expectedrent= models.IntegerField(blank=False)
    expecteddeposit=models.IntegerField(blank=False)
    maintenance = models.CharField(max_length=30)
    availablefrom = models.DateTimeField(blank=False)
    preferedtenants = models.CharField(max_length=50,blank=False)
    furnishing = models.CharField(max_length=20,blank=False)
    parking = models.CharField(max_length=20,blank=False)


class RentImagedetail(models.Model):
    image= models.CharField(max_length=20,blank=True)


    def __str__(self):
        return self.image

class RentAmenities(models.Model):

    bathroom = models.IntegerField()
    balcony = models.IntegerField()
    watersupply=models.CharField(max_length=20)
    gym = models.BooleanField(default=False)
    nonvegallowed = models.BooleanField(default=True)
    showinghouse = models.CharField(max_length=20)
    secondarynumber = models.IntegerField()
    amenitiesavailable=models.CharField(max_length=400)

class ResalePropertyDetail(models.Model):
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

class ResaleLocationDetail(models.Model):
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


class ResaleImagedetail(models.Model):
    image= models.CharField(max_length=20,blank=True)


    def __str__(self):
        return self.image

class ResaleAmenities(models.Model):
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

class ResaleSchedule(models.Model):
    availabilty       = models.CharField(max_length=30)
    startTime         = models.DateTimeField()
    endTime           = models.DateTimeField()
    availabiltyAllDay = models.BooleanField(default=False)

class HostelRoomDetail(models.Model):
    room_choices = [
        ("SINGLE","Single"),
        ("DOUBLE","Double"),
        ("THREE","Three"),
        ("FOUR","Four")
    ]
    roomsavailable = models.CharField(max_length=20,choices=room_choices,blank=False)
    rentexpected = models.IntegerField(blank=False)
    rentDeposit = models.IntegerField(blank=False)
    cupboards = models.BooleanField(default=False)
    Tv = models.BooleanField(default=False)
    bedding = models.BooleanField(default=False)
    geyser = models.BooleanField(default=False)
    Ac = models.BooleanField(default=False)
    attachedbathroom = models.BooleanField(default=False)

class Hostellocation(models.Model):
    roomavailibility  = models.ForeignKey(HostelRoomDetail,on_delete=models.CASCADE)
    city     = models.CharField(max_length=50,blank=False)
    locality = models.CharField(max_length=150,blank=False)
    street   = models.CharField(max_length=150,blank=False)

    def __str__(self):
        return self.city

class Hosteldetails(models.Model):
    hostellocation = models.ForeignKey(Hostellocation,on_delete=models.CASCADE)
    gender_choices = [
        ("Male","MALE"),
        ("Female","FEMALE"),
        ("Anyone","ANYONE")
    ]
    availabiltyfor = models.CharField(choices=gender_choices,max_length=20,blank=False)
    preferedguests = models.CharField(max_length=30,blank=False)
    Availablefrom = models.DateTimeField()
    foodincluded = models.BooleanField(blank=False)
    image = models.ImageField()
    






