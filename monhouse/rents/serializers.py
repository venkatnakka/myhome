from rest_framework import serializers
from .models import *
class PropertySerializer(models.ModelSerializers):
    class Meta:
        model = PropertyDetail
        fields = '__all__'

class LocationSerializer(models.ModelSerializers):
    class Meta:
        model = LocationDetail
        fields = '__all__'

class RentalSerializer(models.ModelSerializers):
    class Meta:
        model = RentalDetail
        fields = '__all__'