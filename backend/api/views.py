from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from apps.main.serializers import (
    CategorySerializer,
    ThingSerializer,
    ImageSerializer,
    UserProfileSerializer,
    TradeSerializer,
    FeedbackSerializer,
)
from apps.main.models import (
    Category,
    Thing,
    Image,
    UserProfile,
    Trade,
    Feedback,
)
from apps.chat.serializers import (
    DialogSerializer,
    MessageSerializer,
)
from apps.chat.models import (
    Dialog,
    Message,
)
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


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ThingViewSet(viewsets.ModelViewSet):
    queryset = Thing.objects.all()
    serializer_class = ThingSerializer

    @action(detail=False, methods=["get"])
    def start(self, request):
        # Получаем последние 6 вещей
        latest_things = Thing.objects.all().order_by("-id")[:6]
        serializer = self.get_serializer(latest_things, many=True)
        return Response(serializer.data)

    def set_image_from_request(self, thing):
        image = self.request.data.get("images")
        if image is not None:
            thing.set_image(image)

    def perform_create(self, serializer):
        self.set_image_from_request(serializer.save())

    def perform_update(self, serializer):
        self.set_image_from_request(serializer.save())


class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer


class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class DialogViewSet(viewsets.ModelViewSet):
    queryset = Dialog.objects.all()
    serializer_class = DialogSerializer


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class TradeViewSet(viewsets.ModelViewSet):
    queryset = Trade.objects.all()
    serializer_class = TradeSerializer


class FeedbackViewSet(viewsets.ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer


class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class RegionViewSet(viewsets.ModelViewSet):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer


class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
