from rest_framework import serializers
from .models import *
class PropertySerializer(serializers.ModelSerializers):
    class Meta:
        model = PropertyDetail
        fields = '__all__'

class LocationSerializer(serializers.ModelSerializers):
    class Meta:
        model = LocationDetail
        fields = '__all__'

class RentalSerializer(serializers.ModelSerializers):
    class Meta:
        model = RentalDetail
        fields = '__all__'
        
class Amenities(serializers.ModelSerializers):
    class Meta:
        model = ResaleAmenities
        fields = '__all__'
