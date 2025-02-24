# Generated by Django 5.1.4 on 2024-12-30 11:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('blogpost', '0001_initial'),
        ('blogtopic', '0001_initial'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog_posts_author', to='user.user'),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog_posts_topic', to='blogtopic.blogtopic'),
        ),
    ]
