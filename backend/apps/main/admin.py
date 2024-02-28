from django.contrib import admin
from .models import *

admin.site.register(Category)
admin.site.register(Thing)

admin.site.register(Location)
admin.site.register(UserProfile)

admin.site.register(Dialog)
admin.site.register(Message)

admin.site.register(Feedback)
admin.site.register(Trade)

admin.site.register(Image)
admin.site.register(Country)

admin.site.register(Region)
admin.site.register(City)
