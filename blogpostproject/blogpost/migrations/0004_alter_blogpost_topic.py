# Generated by Django 5.1.4 on 2025-01-02 15:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogpost', '0003_alter_blogpost_author'),
        ('blogtopic', '0003_alter_blogtopic_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='topic',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='blog_posts_topic', to='blogtopic.blogtopic'),
        ),
    ]
