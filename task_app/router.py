from rest_framework import routers
from .views import TaskListViewSet, TaskViewSet, AttachmentViewSet

app_name = 'task_app'

router = routers.DefaultRouter()
router.register('tasklist', TaskListViewSet)
router.register('tasks', TaskViewSet)
router.register('attachments', AttachmentViewSet)
