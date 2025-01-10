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
        from user.serializers import UserSerializer
        return UserSerializer(obj.author).data    
    
# to work around circular import problem, the imports are moved inside functions    
# https://stackoverflow.com/questions/33413523/circular-dependency-in-django-rest-framework-serializers