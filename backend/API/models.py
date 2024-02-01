from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)


class Thing(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    category_id = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    owner_id = models.ForeignKey(User, on_delete=models.CASCADE)
    images = models.ImageField(upload_to="../media/images")


class Location(models.Model):
    country = models.CharField(max_length=150)
    city = models.CharField(max_length=175)


class UserProfile(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    location_id = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True)


class Dialog(models.Model):
    user_A_id = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="dialog_user_A"
    )
    user_B_id = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="dialog_user_B"
    )
    start_on = models.DateTimeField()


class Message(models.Model):
    dialog_id = models.ForeignKey(Dialog, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)


class Feedback(models.Model):
    text = models.TextField()
    rating = models.IntegerField(null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    user_side = models.TextField()


class Trade(models.Model):
    thing_id = models.ForeignKey(Thing, on_delete=models.CASCADE)
    participant_A_id = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="trade_user_A"
    )
    participant_B_id = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="trade_user_B"
    )
    created_on = models.DateTimeField(auto_now_add=True)
    closed_on = models.DateTimeField()
    feedback_id = models.ForeignKey(Feedback, on_delete=models.CASCADE)
