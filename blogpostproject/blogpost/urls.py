from django.urls import path
from .views import BlogPostListCreateView, BlogPostDetailView

urlpatterns = [
    path('', BlogPostListCreateView.as_view(), name='post-list-create'),
    path('<int:pk>/', BlogPostDetailView.as_view(), name='post-detail'),
]
