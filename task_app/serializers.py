from rest_framework import serializers
from .models import Task, TaskList, Attachment
from house_app.models import House


class TaskListSerializer(serializers.ModelSerializer):
    house = serializers.HyperlinkedRelatedField(queryset=House.objects.all(),
                                                many=False, view_name='house-detail')
    created_by = serializers.HyperlinkedRelatedField(read_only=True,
                                                     many=False, view_name='userprofile-detail')
    tasks = serializers.HyperlinkedRelatedField(read_only=True, many=True, view_name='task-detail')

    class Meta:
        model = TaskList
        fields = ['url', 'id', 'name', 'description',
                  'created_by', 'status', 'house', 'tasks', 'created_at']
        read_only_fields = ['created_by', 'status']


class TaskSerializer(serializers.ModelSerializer):
    created_by = serializers.HyperlinkedRelatedField(read_only=True,
                                                     many=False, view_name='userprofile-detail')
    completed_by = serializers.HyperlinkedRelatedField(read_only=True,
                                                       many=False, view_name='userprofile-detail')
    task_list = serializers.HyperlinkedRelatedField(queryset=TaskList.objects.all(), many=False,
                                                    view_name='tasklist-detail')
    attachment = serializers.HyperlinkedRelatedField(read_only=True, many=True, view_name='attachment-detail')

    class Meta:
        model = Task
        fields = ['url', 'id', 'name', 'description', 'created_by', 'attachment',
                  'completed_by', 'task_list', 'created_at', 'completed_at',
                  'status']
        read_only_fields = ['created_by', 'completed_by', 'created_at',
                            'completed_at']


class AttachmentSerializer(serializers.ModelSerializer):
    task = serializers.HyperlinkedRelatedField(queryset=Task.objects.all(), many=False, view_name='task-detail')

    class Meta:
        model = Attachment
        fields = ['url', 'id', 'task', 'file', 'created_at']
        read_only_field = ['created_at']
