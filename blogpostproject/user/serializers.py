from .models import User
from rest_framework import serializers
    

class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    email = serializers.EmailField()
    group_names = serializers.SerializerMethodField() 
    
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'imageURL', 'group_names']
        
    def get_group_names(self, obj):
        print(f"Full object details: {obj.__dict__}")
        print(f"Executing get_group_names for user: {obj.username}, Groups: {obj.groups.all()}")
        return [group.name for group in obj.groups.all()] or []  # Default to empty list


# obj.groups refers to the related groups for a User object.
# the User model is associated with the Group model through a many-to-many relationship.
# the groups relation exists internally because it is defined in the User model
