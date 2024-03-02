import os
import uuid
from django.db import models
from django.contrib.auth.models import User
import os

from django.conf import settings

MEDIA_ROOT = settings.MEDIA_ROOT
BASE_DIR = settings.BASE_DIR


# Utility class for Images
class Uploader:
    @staticmethod
    def get_or_create_path(name):
        try:
            os.mkdir(str(name))
        except Exception as e:
            print(e)
        finally:
            return str(name)

    @staticmethod
    def get_path(image_type, filename, base_for_file=""):  #owner
        os.chdir(MEDIA_ROOT) # from "/swaphub/media" to "/media"
        
        if image_type:
            os.chdir(Uploader.get_or_create_path(image_type))
        if base_for_file:
            os.chdir(Uploader.get_or_create_path(base_for_file))

        return os.getcwd() + "/" + filename


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


class Image(models.Model):
    local_url = models.ImageField(upload_to=upload_to, default="")
    url_to_upload = models.CharField(max_length=200, default="")
    # created = models.DateTimeField(auto_now_add=True)

    @staticmethod
    def get_uuid_name_with_extension(image):
        # Генерируем уникальное имя для изображения с расширением
        ext = image.name.split(".")[-1]

        return f"{uuid.uuid4()}.{ext}"

    @staticmethod
    def upload_image(image_type, image, base=""): # owner

        image_name = Image.get_uuid_name_with_extension(image)
        picture = Image.objects.create(  # http://localhost/media/ub/media/thing/15/224143e5-bdcf-410e-b162-609bcaa7c18f.png -> http://localhost/media/thing/15/224143e5-bdcf-410e-b162-609bcaa7c18f.png
            local_url=image,             # ub/media/thing/15/224143e5-bdcf-410e-b162-609bcaa7c18f.png -> thing/15/224143e5-bdcf-410e-b162-609bcaa7c18f.png
            url_to_upload=Uploader.get_path(  # /swaphub/media/thing/15/224143e5-bdcf-410e-b162-609bcaa7c18f.png -> http://localhost/media/thing/15/224143e5-bdcf-410e-b162-609bcaa7c18f.png
                image_type, image_name, base_for_file=base
            ),  # owner
        )
        return picture 

    def delete(self, using=None, keep_parents=False):
        os.remove(self.url_to_upload)
        super().delete(using=using, keep_parents=keep_parents)


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
    images = models.ForeignKey(Image, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

    def set_image(self, image):
        image_instance = Image.upload_image(
            #owner=self.owner_id.id,
            #owner=self.owner.id,
            image=image,
            image_type="thing",
            base=self.id,
        )
        self.images = image_instance

        self.save()


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
