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
        # Получаем последние 6 вещей
        latest_things = Thing.objects.all().order_by("-id")[:6]
        serializer = self.get_serializer(latest_things, many=True)
        data = serializer.data

        # Обновляем ссылки на изображения
        for thing_data in data:
            images_data = []
            images = thing_data.get("images")  # Получаем список изображений

            if isinstance(images, list):  # Если это список изображений
                for image_id in images:
                    image = Image.objects.get(pk=image_id)
                    images_data.append(image.local_url.url)
                thing_data["images"] = images_data  # Обновляем ссылки на изображения
            else:  # Если это одиночное изображение
                if images is not None:
                    image = Image.objects.get(pk=images)
                    thing_data["images"] = image.local_url.url

        return Response(data)


    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        data = serializer.data

        # Обновляем ссылки на изображения
        for thing_data in data:
            images_data = []
            images = thing_data.get("images")  # Получаем список изображений

            if isinstance(images, list):  # Если это список изображений
                for image_id in images:
                    image = Image.objects.get(pk=image_id)
                    images_data.append(image.local_url.url)
                thing_data["images"] = images_data  # Обновляем ссылки на изображения
            else:  # Если это одиночное изображение
                if images is not None:
                    image = Image.objects.get(pk=images)
                    thing_data["images"] = image.local_url.url

        return Response(data)

    def set_image_from_request(self, thing):
        image = self.request.data.get("imagess")
        print(image)
        if image is not None:
            thing.set_image(image)

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
