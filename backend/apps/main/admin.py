from django.contrib import admin
from .models import (
    Category,
    Thing,
    Image,
    UserProfile,
    Trade,
    Feedback,
)


admin.site.register(Category)
admin.site.register(Thing)

admin.site.register(UserProfile)

admin.site.register(Feedback)
admin.site.register(Trade)

admin.site.register(Image)
