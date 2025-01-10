from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.exceptions import PermissionDenied

from .models import BlogTopic
from .serializers import BlogTopicSerializer


class BlogTopicListCreateView(generics.ListCreateAPIView):
    queryset = BlogTopic.objects.all()
    serializer_class = BlogTopicSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        # Automatically assign the logged-in user as the author
        serializer.save(author=self.request.user)


class BlogTopicDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogTopic.objects.all()
    serializer_class = BlogTopicSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_update(self, serializer):
        # Prevent unauthorized users from updating
        if self.get_object().author != self.request.user:
            raise PermissionDenied("You do not have permission to edit this topic.")
        serializer.save()

    def perform_destroy(self, instance):
        # Prevent unauthorized users from deleting
        if instance.author != self.request.user:
            raise PermissionDenied("You do not have permission to delete this topic.")
        instance.delete()
