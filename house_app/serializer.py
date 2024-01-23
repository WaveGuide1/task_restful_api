from rest_framework import serializers
from .models import House


class HouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = House
        fields = ['url', 'id', 'name', 'manager', 'created_at', 'description', 'picture',
                  'points', 'task_completed_count', 'task_uncompleted_count']

        read_only_fields = ['task_uncompleted_count', 'task_completed_count', 'points']
