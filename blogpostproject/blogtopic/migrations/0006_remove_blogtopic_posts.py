# Generated by Django 5.1.4 on 2025-01-02 17:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogtopic', '0005_alter_blogtopic_posts'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogtopic',
            name='posts',
        ),
    ]
