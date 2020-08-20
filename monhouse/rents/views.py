from django.shortcuts import render

# Create your views here.
from .serializers import *
from .models import *
from rest_framework import generics

class PropertyView(generics.ListCreateAPIView):
    queryset = PropertyDetail.objects.all()
    serializer_class = PropertySerializer

    def create_new(self,serializer):
        serializer.save()

class PropertyDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PropertyDetail.objects.all()
    serializer_class = PropertySerializer

class LocationView(generics.ListCreateAPIView):
    queryset = LocationDetail.objects.all()
    serializer_class = LocationSerializer

    def create_new(self,serializer):
        serializer.save()

class LocationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = LocationDetail.objects.all()
    serializer_class = LocationSerializer

    