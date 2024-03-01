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
    def get_path(owner, picture_type, filename, base_for_file=""):
        os.chdir(MEDIA_ROOT)
        os.chdir(Uploader.get_or_create_path(owner))
        if picture_type:
            os.chdir(Uploader.get_or_create_path(picture_type))
        if base_for_file:
            os.chdir(Uploader.get_or_create_path(base_for_file))
        return os.getcwd() + "/" + filename


def upload_to(instance, filename):
    relative_path = instance.url_to_upload.rfind("images/") + len("images/")
    return instance.url_to_upload[relative_path:]