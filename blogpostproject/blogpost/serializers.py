from rest_framework import serializers

from blogtopic.models import BlogTopic
from .models import BlogPost


class BlogPostSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(read_only=True)  
    topic = serializers.PrimaryKeyRelatedField(queryset=BlogTopic.objects.all())
    
    class Meta:
        model = BlogPost
        fields = ['id', 'post', 'created_at', 'author', 'topic']