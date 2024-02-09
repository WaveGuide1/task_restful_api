from django.shortcuts import render
from rest_framework import mixins, viewsets, filters
from .models import TaskList, Task, Attachment, NOT_COMPLETE, COMPLETE
from .serializers import TaskListSerializer, TaskSerializer, AttachmentSerializer
from .permissions import IsTaskListCreator, IsTaskEditingAllowed, IsAttachmentEditingAllowed
from rest_framework.decorators import action
from django.utils import timezone
from rest_framework.response import Response
from rest_framework import status as st
from django_filters.rest_framework import DjangoFilterBackend


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
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['=name', 'description']
    filterset_fields = ['status',]

    def get_queryset(self):
        queryset = super(TaskViewSet, self).get_queryset()
        user_profile = self.request.user.userprofile
        new_queryset = queryset.filter(created_by=user_profile)
        return new_queryset

    # Update task status
    @action(methods=['patch'], detail=True)
    def update_task_status(self, request, pk=None):

        try:
            task = self.get_object()
            user_profile = self.request.user.userprofile
            status = request.data['status']
            if status == NOT_COMPLETE:
                if task.status == COMPLETE:
                    task.status = NOT_COMPLETE
                    task.completed_by = None
                    task.completed_at = None
                else:
                    return Response({'message': 'Task is already marked not Completed'})
            elif status == COMPLETE:
                if task.status == NOT_COMPLETE:
                    task.status = COMPLETE
                    task.completed_at = timezone.now()
                    task.completed_by = user_profile
                else:
                    return Response({'message': 'Task is already marked Completed'})
            else:
                return Response({'message': 'Incorrect task status'})
            task.save()
            serializer = TaskSerializer(instance=task, context={'request': request})
            return Response(serializer.data, status=st.HTTP_200_OK)
        except Exception as err:
            return Response({'message': 'Bad request'}, status=st.HTTP_400_BAD_REQUEST)


class AttachmentViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin,
                        mixins.RetrieveModelMixin, mixins.DestroyModelMixin,
                        mixins.UpdateModelMixin):
    queryset = Attachment.objects.all()
    serializer_class = AttachmentSerializer
    permission_classes = [IsAttachmentEditingAllowed]
