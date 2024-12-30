from rest_framework import serializers
from django.db import models

from blogpost.models import BlogPost
from user.serializers import UserSerializer
from .models import BlogTopic

class BlogTopicSerializer(serializers.ModelSerializer):
    title = models.CharField(max_length=255)
    author = UserSerializer(read_only=True)
    posts = serializers.PrimaryKeyRelatedField(many=True, queryset=BlogPost.objects.all(), required=False)
    
    class Meta:
        model = BlogTopic
        fields = ['id', 'title', 'author', 'posts']