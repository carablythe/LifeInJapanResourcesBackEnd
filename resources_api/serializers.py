from rest_framework import serializers
from .models import Resource, Forum


class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resource
        fields = ('id', 'topic', 'category', 'subcategory', 'URL', 'description',)


class ForumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Forum
        fields = ('id', 'name', 'question',)
