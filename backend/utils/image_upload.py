import os
from django.conf import settings

MEDIA_URL = settings.MEDIA_URL
BASE_DIR = settings.BASE_DIR


class Uploader:
    ''' Utility class for Images '''

    @staticmethod
    def get_or_create_path(name):
        try:
            os.mkdir(str(name))
        except Exception as e:
            print(e)
        finally:
            return str(name)

    @staticmethod
    def get_path(owner, image_type, filename, base_for_file=""):
        os.chdir(MEDIA_URL)

        if owner:
            os.chdir(Uploader.get_or_create_path(owner))
        if image_type:
            os.chdir(Uploader.get_or_create_path(image_type))
        if base_for_file:
            os.chdir(Uploader.get_or_create_path(base_for_file))

        path = os.getcwd()

        return f'{path}/{filename}'


def upload_to(instance, filename):

    host = settings.ALLOWED_HOSTS[0]
    extra_part_index = len(f'{host}/media/')

    upload_path = instance.url_to_upload[extra_part_index:]

    return upload_path
