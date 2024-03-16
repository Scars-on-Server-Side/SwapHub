import os
import uuid

from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

from apps.loc.models import Location
from utils.image_upload import Uploader, upload_to


class UserProfile(models.Model):
    '''
    Override base class User
    '''

    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return str(self.user.username)


class Category(models.Model):
    '''
    Things categories
    '''

    parent = models.IntegerField(default=0)
    name = models.CharField(max_length=350)

    def __str__(self):
        return self.name


class Thing(models.Model):

    name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    avatar = models.CharField(max_length=300, default="")

    def __str__(self):
        return self.name

    def set_image(self, images):
        Image.upload_image(
            owner=self.owner.id,
            image_type="thing",
            thing=self,
            images=images,
            base=self.id,
        )

    def set_avatar(self):
        self.avatar = Image.objects.filter(thing__id=self.id).first().url_to_upload
        self.save()


class Image(models.Model):
    local_url = models.ImageField(upload_to=upload_to, default="")
    url_to_upload = models.CharField(max_length=200, default="")
    thing = models.ForeignKey(Thing, on_delete=models.SET_NULL, null=True)
    created_on = models.DateTimeField(auto_now_add=True)

    @staticmethod
    def get_uuid_name_with_extension(image):
        # Генерируем уникальное имя для изображения с расширением
        extension = image.name.split(".")[-1]
        return f"{uuid.uuid4()}.{extension}"

    @staticmethod
    def upload_image(owner, image_type, thing, images, base=""):

        host = settings.ALLOWED_HOSTS[0]

        for image in images:
            image_name = Image.get_uuid_name_with_extension(image)

            Image.objects.create(
                local_url=image,
                url_to_upload=host + Uploader.get_path(
                    owner,
                    image_type,
                    image_name,
                    base_for_file=base
                ),
                thing=thing
            )

    def delete(self, using=None, keep_parents=False):
        os.remove(self.url_to_upload)
        super().delete(using=using, keep_parents=keep_parents)


class Trade(models.Model):

    thing = models.ForeignKey(Thing, on_delete=models.CASCADE)
    participant_A = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="trade_user_A"
    )
    participant_B = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="trade_user_B"
    )
    created_on = models.DateTimeField(auto_now_add=True)
    closed_on = models.DateTimeField(blank=True, null=True)


class Feedback(models.Model):

    text = models.TextField()
    rating = models.IntegerField(null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    trade = models.ForeignKey(Trade, on_delete=models.CASCADE)

    def __str__(self):
        return self.text
