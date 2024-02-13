from django.db import models
from django.utils.deconstruct import deconstructible
import os
import uuid

# Create your models here.

@deconstructible
class FilePathGenerator(object):

    def __init__(self):
        pass

    def __call__(self, instance, filename):
        file_extension = filename.split('.')[-1]
        filepath = f"media/house/{instance.id}/images/"
        picture_name = f"house_picture.{file_extension}"
        return os.path.join(filepath, picture_name)


house_picture_path = FilePathGenerator()


class House(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid1, editable=False)
    name = models.CharField(max_length=225)
    picture = models.FileField(upload_to=house_picture_path, blank=True, null=True)
    description = models.TextField()
    manager = models.OneToOneField('user_app.userprofile', on_delete=models.SET_NULL,
                                   blank=True, null=True, related_name='house_manager')
    points = models.IntegerField(default=0)
    task_completed_count = models.IntegerField(default=0)
    task_uncompleted_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
