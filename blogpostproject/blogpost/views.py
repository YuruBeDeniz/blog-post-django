from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.exceptions import PermissionDenied
from rest_framework import serializers

from blogtopic.models import BlogTopic
from .models import BlogPost
from .serializers import BlogPostSerializer


class BlogPostListCreateView(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def get_queryset(self):
        queryset = super().get_queryset()
        topic_id = self.request.query_params.get('topic', None)
        print(f"Received topic_id: {topic_id}")
        if topic_id:
            queryset = queryset.filter(topic_id=topic_id)
        return queryset

    def perform_create(self, serializer):
        print(f"Request data: {self.request.data}")
        topic_id = self.request.data.get('topic')
        topic = BlogTopic.objects.filter(id=topic_id).first()
    
        if not topic:
            raise serializers.ValidationError("Invalid topic ID")
    
        serializer.save(author=self.request.user, topic=topic)
    

class BlogPostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_update(self, serializer):
        # Prevent unauthorized users from updating
        if self.get_object().author != self.request.user:
            raise PermissionDenied("You do not have permission to edit this post.")
        serializer.save()

    def perform_destroy(self, instance):
        # Prevent unauthorized users from deleting
        if instance.author != self.request.user:
            raise PermissionDenied("You do not have permission to delete this post.")
        instance.delete()

