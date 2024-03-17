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


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ThingViewSet(viewsets.ModelViewSet):
    queryset = Thing.objects.all()
    serializer_class = ThingSerializer

    @action(detail=False, methods=["get"])
    def start(self, request):
        # Эндпоинт стартовой страницы, которая отображает последние 6 добавленных вещей

        latest_things = Thing.objects.all().order_by("-id")[:6]
        serializer = self.get_serializer(latest_things, many=True)

        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)

        out_data = serializer.data
        out_data["images"] = ImageSerializer(Image.objects.filter(thing__id=out_data["id"]), many=True).data

        return Response(out_data)

    def set_image_from_request(self, thing):
        images = self.request.data.getlist("image")

        if (images is not None) and (images != []):
            thing.set_image(images)
            thing.set_avatar()

    def perform_create(self, serializer):
        self.set_image_from_request(serializer.save())

    def perform_update(self, serializer):
        self.set_image_from_request(serializer.save())


class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class TradeViewSet(viewsets.ModelViewSet):
    queryset = Trade.objects.all()
    serializer_class = TradeSerializer


class FeedbackViewSet(viewsets.ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
