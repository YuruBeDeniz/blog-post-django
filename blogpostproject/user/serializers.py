from .models import User
from rest_framework import serializers
    

class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    email = serializers.EmailField()
    
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'imageURL']
