from rest_framework import serializers
from .models import BlogPost


class SimplifiedBlogPostSerializer(serializers.Serializer):
    post = serializers.CharField()
    created_at = serializers.DateTimeField()
    
class BlogPostSerializer(serializers.ModelSerializer):
    topic = serializers.SerializerMethodField()
    author = serializers.SerializerMethodField()

    class Meta:
        model = BlogPost
        fields = ['id', 'post', 'created_at', 'author', 'topic']

    def get_topic(self, obj):
        from blogtopic.serializers import SimplifiedBlogTopicSerializer
        return SimplifiedBlogTopicSerializer(obj.topic).data

    def get_author(self, obj):
        from user.serializers import SimplifiedUserSerializer
        return SimplifiedUserSerializer(obj.author).data    