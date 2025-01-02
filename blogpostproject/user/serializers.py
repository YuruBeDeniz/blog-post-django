from .models import User
from rest_framework import serializers


class SimplifiedUserSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.EmailField()

class UserSerializer(serializers.ModelSerializer):
    posts = serializers.SerializerMethodField()
    topics = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'posts', 'topics', 'imageURL']

    def get_posts(self, obj):
        from blogpost.serializers import SimplifiedBlogPostSerializer
        return SimplifiedBlogPostSerializer(obj.posts.all(), many=True).data

    def get_topics(self, obj):
        from blogtopic.serializers import SimplifiedBlogTopicSerializer
        return SimplifiedBlogTopicSerializer(obj.topics.all(), many=True).data