from django.conf import settings
from django.db import models
from django.apps import apps

def get_default_user():
    User = apps.get_model(settings.AUTH_USER_MODEL)
    return User.objects.get(username="default_user").id


class BlogTopic(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(
        'user.User', 
        related_name='blog_topics_author', 
        on_delete=models.CASCADE, 
        default=get_default_user
    )
    posts = models.ManyToManyField('blogpost.BlogPost', related_name='blog_topics_posts', blank=True)

    def __str__(self):
        return self.title
    
