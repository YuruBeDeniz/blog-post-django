from django.urls import path
from .views import BlogTopicListCreateView, BlogTopicDetailView

urlpatterns = [
    path('', BlogTopicListCreateView.as_view(), name='topic-list-create'),
    path('<int:pk>/', BlogTopicDetailView.as_view(), name='topic-detail'),
]
