from django.db import models

# Create your models here.
COMPLETE = 'CP'
NOT_COMPLETE = 'NC'
PENDING = 'PD'

STATUS_CHOICE = [
    (COMPLETE, 'complete'),
    (NOT_COMPLETE, 'completed'),
    (PENDING, 'pending'),
]


class Task(models.Model):
    name = models.CharField(max_length=225)
    description = models.TextField(null=True, blank=True)
    created_by = models.ForeignKey('user_app.userprofile', null=True, blank=True,
                                   on_delete=models.SET_NULL, related_name='created_tasks')
    completed_by = models.ForeignKey('user_app.userprofile', null=True, blank=True,
                                     on_delete=models.SET_NULL, related_name='completed_tasks')
    created_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=2, default=NOT_COMPLETE, choices=STATUS_CHOICE)

    def __str__(self):
        return self.name
