from django.shortcuts import render
from rest_framework import mixins, viewsets
from .models import TaskList, Task, Attachment
from .serializers import TaskListSerializer, TaskSerializer, AttachmentSerializer
from .permissions import IsTaskListCreator, IsTaskEditingAllowed, IsAttachmentEditingAllowed
from rest_framework.decorators import action


# Create your views here.


class TaskListViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.DestroyModelMixin, mixins.UpdateModelMixin):
    queryset = TaskList.objects.all()
    serializer_class = TaskListSerializer
    permission_classes = [IsTaskListCreator]


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsTaskEditingAllowed]

    def get_queryset(self):
        queryset = super(TaskViewSet, self).get_queryset()
        user_profile = self.request.user.userprofile
        new_queryset = queryset.filter(created_by=user_profile)
        return new_queryset

    @action(methods=['patch'], detail=True)
    def update_task_status(self):

        try:
            task = self.get_object()
            user_profile = self.user.userprofile
        except Exception as err:
            pass


class AttachmentViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin,
                        mixins.RetrieveModelMixin, mixins.DestroyModelMixin,
                        mixins.UpdateModelMixin):
    queryset = Attachment.objects.all()
    serializer_class = AttachmentSerializer
    permission_classes = [IsAttachmentEditingAllowed]
