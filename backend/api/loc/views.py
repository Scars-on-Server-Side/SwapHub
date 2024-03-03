from rest_framework import viewsets

from apps.loc.serializers import (
    LocationSerializer,
    CountrySerializer,
    RegionSerializer,
    CitySerializer,
)
from apps.loc.models import (
    Location,
    Country,
    Region,
    City,
)


class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class RegionViewSet(viewsets.ModelViewSet):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer


class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer


class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
