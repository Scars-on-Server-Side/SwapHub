from rest_framework import serializers
from .models import *


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class ThingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Thing
        fields = "__all__"


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = "__all__"


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = "__all__"


class DialogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dialog
        fields = "__all__"


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = "__all__"


class TradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trade
        fields = "__all__"


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = "__all__"
