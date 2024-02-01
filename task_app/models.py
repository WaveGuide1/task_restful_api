from django.db import models
import uuid
import os
from django.utils.deconstruct import deconstructible

# Create your models here.
COMPLETE = 'CP'
NOT_COMPLETE = 'NC'
PENDING = 'PD'

STATUS_CHOICE = [
    (NOT_COMPLETE, 'Not completed'),
    (COMPLETE, 'complete'),
    (PENDING, 'pending'),
]


@deconstructible
class FilePathGenerator(object):
    def __init__(self):
        pass

    def __call__(self, instance, filename):
        file_extension = filename.split('.')[-1]
        filepath = f"media/task/{instance.task.id}/attachments/"
        file_name = f"attach_file.{file_extension}"
        return os.path.join(filepath, file_name)


class TaskList(models.Model):
    name = models.CharField(max_length=225)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(blank=True, null=True)
    created_by = models.ForeignKey('user_app.userprofile', null=True, blank=True,
                                   on_delete=models.SET_NULL, related_name='lists')
    house = models.ForeignKey('house_app.House', on_delete=models.CASCADE,
                              related_name='lists')
    status = models.CharField(max_length=2, default=NOT_COMPLETE, choices=STATUS_CHOICE)

    def __str__(self):
        return self.name


class Task(models.Model):
    name = models.CharField(max_length=225)
    description = models.TextField(null=True, blank=True)
    created_by = models.ForeignKey('user_app.userprofile', null=True, blank=True,
                                   on_delete=models.SET_NULL, related_name='created_tasks')
    completed_by = models.ForeignKey('user_app.userprofile', null=True, blank=True,
                                     on_delete=models.SET_NULL, related_name='completed_tasks')
    task_list = models.ForeignKey('task_app.TaskList', on_delete=models.CASCADE, related_name='tasks')
    created_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=2, default=NOT_COMPLETE, choices=STATUS_CHOICE)

    def __str__(self):
        return self.name


file_path = FilePathGenerator()


class Attachment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    task = models.ForeignKey('task_app.Task', on_delete=models.CASCADE,
                             related_name='attachment')
    file = models.FileField(upload_to=file_path, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.task)
