from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import Group
from .models import User

@receiver(post_save, sender=User)
def assign_default_group(sender, instance, created, **kwargs):
    print(f"Signal triggered for user: {instance.username}")
    if created:
        print("User created. Assigning default group...")
        regular_user_group, _ = Group.objects.get_or_create(name='RegularUser')
        instance.groups.add(regular_user_group)
        print(f"Groups after assignment: {instance.groups.all()}")
