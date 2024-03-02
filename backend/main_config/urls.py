"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

from api.views import (
    CategoryViewSet,
    ThingViewSet,
    LocationViewSet,
    UserProfileViewSet,
    DialogViewSet,
    MessageViewSet,
    TradeViewSet,
    FeedbackViewSet,
    CountryViewSet,
    RegionViewSet,
    CityViewSet,
    ImageViewSet
)


router = routers.SimpleRouter()
router.register(r"category", CategoryViewSet)
router.register(r"thing", ThingViewSet)
router.register(r"location", LocationViewSet)
router.register(r"userprofile", UserProfileViewSet)

router.register(r"dialog", DialogViewSet)
router.register(r"message", MessageViewSet)
router.register(r"trade", TradeViewSet)
router.register(r"feedback", FeedbackViewSet)

router.register(r"country", CountryViewSet)
router.register(r"region", RegionViewSet)
router.register(r"city", CityViewSet)
router.register(r"image", ImageViewSet)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include(router.urls)),
    path("api/v1/drf-auth/", include("rest_framework.urls")),
]
