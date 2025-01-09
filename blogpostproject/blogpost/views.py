from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.exceptions import PermissionDenied
from rest_framework import serializers

from blogtopic.models import BlogTopic
from .models import BlogPost
from .serializers import BlogPostSerializer
from .permissions import IsAuthorOrAdmin

import logging

logger = logging.getLogger('django')


class BlogPostListCreateView(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorOrAdmin]
    
    def get_queryset(self):
        queryset = super().get_queryset()
        topic_id = self.request.query_params.get('topic', None)
        print("self.request", self.request)
        if topic_id:
            queryset = queryset.filter(topic_id=topic_id)
        return queryset
    
    def get(self, request, *args, **kwargs):
        logger.info(f"Headers: {request.headers}")
        logger.info(f"Request User: {request.user}, Is Authenticated: {request.user.is_authenticated}")
        return super().get(request, *args, **kwargs)


    def perform_create(self, serializer):
        print(f"Request data: {self.request.data}")
        topic_id = self.request.data.get('topic')
        topic = BlogTopic.objects.filter(id=topic_id).first()
        # first() Returns the first value or None if no objects match, avoiding the need to handle exceptions as opposed to get()
    
        if not topic:
            raise serializers.ValidationError("Invalid topic ID")
    
        serializer.save(author=self.request.user, topic=topic)
        print("self.request", self.request)
        print("self.request.user", self.request.user)
        # save() Passes the validated data, including author and topic, to the BlogPost model

class BlogPostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorOrAdmin]

    def perform_update(self, serializer):
        # Prevent unauthorized users from updating
        # Check if the user is an admin or the author of the post
        if not (self.get_object().author == self.request.user or 
                self.request.user.groups.filter(name='Admin').exists()):
            raise PermissionDenied("You do not have permission to edit this post.")
        serializer.save()

    def perform_destroy(self, instance):
        # Prevent unauthorized users from deleting
        if not (instance.author == self.request.user or 
                self.request.user.groups.filter(name='Admin').exists()):
            raise PermissionDenied("You do not have permission to delete this post.")
        instance.delete()


# The reason saving a BlogPost instance (with its associated topic)
# effectively saves the post with the correct topic is due to how Django ORM 
# (Object-Relational Mapping) handles relationships between models.


# The topic relationship is defined in the BlogPost model as a ForeignKey. This means:
# A BlogPost references a single BlogTopic through the topic field.
# The database stores the topic_id in the blogpost table to indicate the association.