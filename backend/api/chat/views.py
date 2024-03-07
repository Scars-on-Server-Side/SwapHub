from rest_framework import viewsets

from apps.chat.serializers import (
    DialogSerializer,
    MessageSerializer,
)
from apps.chat.models import (
    Dialog,
    Message,
)


class DialogViewSet(viewsets.ModelViewSet):
    queryset = Dialog.objects.all()
    serializer_class = DialogSerializer


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
