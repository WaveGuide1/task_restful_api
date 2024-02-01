from rest_framework import serializers
from .models import House


class HouseSerializer(serializers.ModelSerializer):
    manager = serializers.HyperlinkedRelatedField(many=False, read_only=True, view_name='userprofile-detail')
    members = serializers.HyperlinkedRelatedField(read_only=True, view_name='userprofile-detail', many=True)
    members_count = serializers.IntegerField(read_only=True)
    tasklist = serializers.HyperlinkedRelatedField(read_only=True, many=True, view_name='tasklist-detail', source='lists')

    class Meta:
        model = House
        fields = ['url', 'id', 'name', 'manager', 'members', 'created_at', 'description', 'picture',
                  'points', 'members_count', 'task_completed_count', 'task_uncompleted_count', 'tasklist']

        read_only_fields = ['task_uncompleted_count', 'task_completed_count', 'points']
