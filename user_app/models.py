from django.db import models
import os
from django.utils.deconstruct import deconstructible
from django.contrib.auth.models import User


# Create your models here.

@deconstructible
class FilePathGenerator(object):

    def __init__(self):
        pass

    def __call__(self, instance, filename):
        file_extension = filename.split('.')[-1]
        filepath = f"media/{instance.user.id}/images/"
        picture_name = f"profile_picture.{file_extension}"
        return os.path.join(filepath, picture_name)


user_profile_picture_path = FilePathGenerator()


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.FileField(user_profile_picture_path, null=True, blank=True)
    house = models.ForeignKey('house_app.House', on_delete=models.SET_NULL, blank=True, null=True, related_name='members')

    def __str__(self):
        return self.user.username
