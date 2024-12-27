from django.contrib.auth.models import User
from rest_framework import serializers

from blogpost.models import BlogPost
from blogtopic.models import BlogTopic

class UserSerializer(serializers.ModelSerializer):
    # posts = BlogPostSerializer(many=True, read_only=True)
    # topics = BlogTopicSerializer(many=True, read_only=True)
    posts = serializers.PrimaryKeyRelatedField(many=True, queryset=BlogPost.objects.all())
    topics = serializers.PrimaryKeyRelatedField(many=True, queryset=BlogTopic.objects.all())


    class Meta:
        model = User
        fields = ['id','username', 'email', 'password', 'posts', 'topics', 'imageURL']