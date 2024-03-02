from django.contrib import admin
from .models import (
    Country,
    Region,
    City,
    Location,
)


admin.site.register(Country)
admin.site.register(Region)
admin.site.register(City)
admin.site.register(Location)
