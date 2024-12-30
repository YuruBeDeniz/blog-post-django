from .models import User
from rest_framework import serializers

from blogpost.models import BlogPost
from blogtopic.models import BlogTopic

class UserSerializer(serializers.ModelSerializer):
    posts = serializers.PrimaryKeyRelatedField(many=True, queryset=BlogPost.objects.all())
    topics = serializers.PrimaryKeyRelatedField(many=True, queryset=BlogTopic.objects.all())


    class Meta:
        model = User
        fields = ['id','username', 'email', 'password', 'posts', 'topics', 'imageURL']