from rest_framework import serializers
from .models import Todo

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['id', 'title', 'completed']

    def update(self, instance, validated_data):
        instance.completed = validated_data.get('completed', instance.completed)
        instance.title = validated_data.get('title', instance.title)
        instance.save()
        return instance
