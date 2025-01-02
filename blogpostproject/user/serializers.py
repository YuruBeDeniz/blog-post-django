from .models import User
from rest_framework import serializers


class SimplifiedUserSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.EmailField()

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'imageURL']
