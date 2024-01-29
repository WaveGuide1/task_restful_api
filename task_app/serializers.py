from rest_framework import serializers
from .models import Task, TaskList, Attachment
from house_app.models import House


class TaskListSerializer(serializers.ModelSerializer):
    house = serializers.HyperlinkedRelatedField(queryset=House.objects.all(),
                                                many=False, view_name='house-detail')
    created_by = serializers.HyperlinkedRelatedField(read_only=True,
                                                     many=False, view_name='userprofile-detail')

    class Meta:
        model = TaskList
        fields = ['url', 'id', 'name', 'description',
                  'created_by', 'status', 'house', 'created_at']
        read_only_fields = ['created_by', 'status']


class TaskSerializer(serializers.ModelSerializer):
    pass
