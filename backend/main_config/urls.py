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
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework_simplejwt import views

from api.main.views import (
    CategoryViewSet,
    ThingViewSet,
    UserProfileViewSet,
    TradeViewSet,
    FeedbackViewSet,
    ImageViewSet
)
from api.chat.views import (
    DialogViewSet,
    MessageViewSet,
)
from api.loc.views import (
    CountryViewSet,
    RegionViewSet,
    CityViewSet,
    LocationViewSet,
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
     path('api/v1/token/', views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', views.TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/token/verify/', views.TokenVerifyView.as_view(), name='token_verify'),

    path(
        'api/schema/',
        SpectacularAPIView.as_view(),
        name='schema'),
    path(
        'api/schema/swagger-ui/',
        SpectacularSwaggerView.as_view(url_name='schema'),
        name='swagger-ui'
    ),
]
