from django.db import models
from django.contrib.auth.models import User


class Country(models.Model):

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Region(models.Model):

    name = models.CharField(max_length=250)
    country_id = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class City(models.Model):

    name = models.CharField(max_length=100)
    region_id = models.ForeignKey(Region, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Location(models.Model):

    country_id = models.ForeignKey(Country, on_delete=models.CASCADE, default=None)

    # Необходимо, чтобы после выбора страны были доступны только ее регионы
    region_id = models.ForeignKey(Region, on_delete=models.CASCADE, default=None)
    # Также и с городами
    city_id = models.ForeignKey(City, on_delete=models.CASCADE, default=None)

    def __str__(self) -> int:
        return str(self.country_id.id)


class UserProfile(models.Model):
    '''
    Override base class User
    '''

    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
    location_id = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True)


class Category(models.Model):
    '''
    Things categories
    parent_id - common name of things
    '''

    parent_id = models.IntegerField(default=0)
    name = models.CharField(max_length=350, unique=True)

    def __str__(self) -> str:
        return self.name


""" class ThingImage(models.Model):

    name = models.CharField(max_length=200)

    image = models.ImageField(upload_to="images")

    def __str__(self) -> str:
        return self.name """


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
    image = models.ImageField(upload_to="images", null=True)

    def __str__(self) -> str:
        return self.name


class Dialog(models.Model):

    user_A_id = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="dialog_user_A"
    )
    user_B_id = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="dialog_user_B"
    )
    start_on = models.DateTimeField(auto_now_add=True)


class Message(models.Model):

    dialog_id = models.ForeignKey(Dialog, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.text


class Trade(models.Model):

    thing_id = models.ForeignKey(Thing, on_delete=models.CASCADE)
    participant_A_id = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="trade_user_A"
    )
    participant_B_id = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="trade_user_B"
    )
    created_on = models.DateTimeField(auto_now_add=True)    
    closed_on = models.DateTimeField(blank=True, null=True)


class Feedback(models.Model):

    text = models.TextField()
    rating = models.IntegerField(null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    trade_id = models.ForeignKey(Trade, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.text
