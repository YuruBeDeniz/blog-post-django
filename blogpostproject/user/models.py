from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    email = models.EmailField(unique=True)
    imageURL = models.URLField(max_length=500, blank=True, null=True)
    posts = models.ManyToManyField('blogpost.BlogPost', related_name='user_blog_posts', blank=True)
    topics = models.ManyToManyField('blogtopic.BlogTopic', related_name='user_blog_topics', blank=True)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions_set',
        blank=True
    )

    def __str__(self):
        return self.username