from django.shortcuts import render
from rest_framework import mixins, viewsets
from .models import TaskList, Task, Attachment
from .serializers import TaskListSerializer
from .permissions import IsTaskListCreator

# Create your views here.


class TaskListViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin,
                      mixins.ListModelMixin, mixins.RetrieveModelMixin,
                      mixins.DestroyModelMixin, mixins.UpdateModelMixin):
    queryset = TaskList.objects.all()
    serializer_class = TaskListSerializer
    permission_classes = [IsTaskListCreator]