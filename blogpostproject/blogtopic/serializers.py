from rest_framework import serializers
from .models import BlogTopic

class SimplifiedBlogTopicSerializer(serializers.Serializer):
    title = serializers.CharField()

        
class BlogTopicSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()

    class Meta:
        model = BlogTopic
        fields = ['id', 'title', 'author']

    def get_author(self, obj):
        from user.serializers import UserSerializer
        return UserSerializer(obj.author).data

    def get_posts(self, obj):
        from blogpost.serializers import SimplifiedBlogPostSerializer
        return SimplifiedBlogPostSerializer(obj.posts.all(), many=True).data

# Here posts are serialized and we dont need to initialize them in the BlogTopic model        