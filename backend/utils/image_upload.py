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


def upload_to(instance, filename):
    relative_path = instance.url_to_upload.rfind("images/") + len("images/")
    return instance.url_to_upload[relative_path:]
