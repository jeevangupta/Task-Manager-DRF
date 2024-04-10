from rest_framework import serializers
from .models import Tasks


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = "__all__"

    def validate(self, data):

        if len(data["title"]) == 0:
            raise serializers.ValidationError('Task title cannot be empty!')
        
        if data['status'] not in ["Done", "To Do", "In Progress"]:
            raise serializers.ValidationError('Invalid task status!')
        
        return data

