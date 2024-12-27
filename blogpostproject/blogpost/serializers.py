from django.contrib.auth.models import User
from rest_framework import serializers

from .models import BlogPost


class BlogPostSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(read_only=True)  
    topic = serializers.PrimaryKeyRelatedField(read_only=True)
    
    class Meta:
        model = BlogPost
        fields = ['id', 'post', 'created_at', 'author', 'topic']