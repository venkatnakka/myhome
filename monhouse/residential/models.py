from django.db import models
from residential.mymodels import *


# Create your models here.
class RentPropertyDetail(PropertyDetail):
    facing        = models.CharField(max_length=20,blank=True)
    datecreated = models.DateTimeField(auto_now_add=True,null=True)


class RentLocationDetail(LocationDetail):
    propertydetails = models.ForeignKey(RentPropertyDetail,on_delete= models.CASCADE,null=True)
    street = models.CharField(max_length=150,blank=False)
    


class RentalDetail(models.Model):
    rentallocation = models.ForeignKey(RentLocationDetail,on_delete= models.CASCADE,null=True)
    availablelease= models.BooleanField(default=True)
    expectedrent= models.IntegerField(blank=False)
    expecteddeposit=models.IntegerField(blank=False)
    maintenance = models.CharField(max_length=30)
    availablefrom = models.DateTimeField(blank=False)
    preferedtenants = models.CharField(max_length=50,blank=False)
    furnishing = models.CharField(max_length=20,blank=False)
    parking = models.CharField(max_length=20,blank=False)
    image= models.ImageField()


class RentAmenities(Amenities):
    rentdetails = models.ForeignKey(RentalDetail,on_delete=models.CASCADE)

class RentSchedule(Schedule):
    Rentdetail=models.ForeignKey(RentalDetail,on_delete=models.CASCADE)

class ResalePropertyDetail(PropertyDetail):
    ownershiptype = models.CharField(max_length=20)
    propertyage   = models.CharField(max_length=50)
    floortype     = models.CharField(max_length=30)
    no_of_units   = models.IntegerField()
    facing        = models.CharField(max_length=20,blank=True)
    

class ResaleLocationDetail(LocationDetail):
    Resalepropertydetail = models.ForeignKey(ResalePropertyDetail,on_delete=models.CASCADE)
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
    image= models.ImageField()

class ResaleAmenities(Schedule):
    resaledetail = models.ForeignKey(Resaledetail,on_delete=models.CASCADE)
    

class AdditionalInformation(models.Model):
    saleDeedCertificate  = models.BooleanField(default=True)
    propertytax          = models.BooleanField(default=True)
    occupancyCertificate = models.BooleanField(default=True)

class ResaleSchedule(Schedule):
    resaledetail=models.ForeignKey(Resaledetail,on_delete=models.CASCADE)

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

class Hostellocation(LocationDetail):
    roomavailibility  = models.ForeignKey(HostelRoomDetail,on_delete=models.CASCADE)
    street   = models.CharField(max_length=150,blank=False)


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
    # available services
    # available amenities
    parking_choices = [
        ("TWO WHEELER","Two wheeler"),
        ("FOUR WHEELER","Four wheeler")
    ]
    parking = models.CharField(choices=parking_choices,max_length=20)

class hostelSchedule(Schedule):
    hostelschedule= models.ForeignKey(Hosteldetails,on_delete=models.CASCADE)

class flatDetail(PropertyDetail):
    propertyage   = models.CharField(max_length=50)
    facing        = models.CharField(max_length=20,blank=True)
    propertysize  = models.IntegerField(blank=False)
    tenant_choices = [
        ("MALE","Male"),
        ("FEMALE","Female"),
    ]
    tenant_type = models.CharField(choices=tenant_choices,max_length=20,blank=False)
    Room_choices = [
        ("SINGLE","Single"),
        ("SHAREDROOM","Shared Room")
    ]
    flatrentexpected = models.IntegerField(blank=False)
    flatrentDeposit = models.IntegerField(blank=False)
    










