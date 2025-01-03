from django.apps import apps
from django.conf import settings
from django.db import models

def get_default_user():
    # Get the actual user model class
    User = apps.get_model(settings.AUTH_USER_MODEL)
    # Fetch the user with the username "default_user"
    return User.objects.get(username="default_user").id

def get_default_topic():
    from blogtopic.models import BlogTopic
    return BlogTopic.objects.get_or_create(title="General")[0].id

class BlogPost(models.Model):
    post = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        'user.User', 
        related_name='blog_posts_author', 
        on_delete=models.CASCADE, 
        default=get_default_user
    )
    topic = models.ForeignKey(
        'blogtopic.BlogTopic', 
        related_name='blog_posts_topic', 
        on_delete=models.CASCADE, 
        default=get_default_topic
    )

    def __str__(self):
        return f"Post by {self.author.username} on {self.topic.title}"

# related_name='blog_posts_topic' creates a reverse relationship. 
# This allows you to access all posts for a specific topic using
# topic.blog_posts_topic.all()

# If you don’t specify a related_name, 
# Django automatically generates a name based on the model name:
# blogpost_set: Example: topic.blogpost_set.all()