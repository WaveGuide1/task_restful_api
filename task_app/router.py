from rest_framework import routers
from .views import TaskListViewSet

app_name = 'task_app'

router = routers.DefaultRouter()
router.register('tasklist', TaskListViewSet)