from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from blogpost.models import BlogPost  # Adjust this import based on your project structure

class Command(BaseCommand):
    help = "Setup groups and permissions for the application"

    def handle(self, *args, **kwargs):
        # Create groups
        admin_group, _ = Group.objects.get_or_create(name='Admin')
        user_group, _ = Group.objects.get_or_create(name='RegularUser')

        # Define BlogPost model permissions
        content_type = ContentType.objects.get_for_model(BlogPost)

        can_crud_all, _ = Permission.objects.get_or_create(
            codename='can_crud_all',
            name='Can perform CRUD operations on all posts',
            content_type=content_type
        )

        can_crud_own, _ = Permission.objects.get_or_create(
            codename='can_crud_own',
            name='Can perform CRUD operations only on own posts',
            content_type=content_type
        )

        # Assign permissions to groups
        admin_group.permissions.add(can_crud_all)
        user_group.permissions.add(can_crud_own)

        self.stdout.write(self.style.SUCCESS("Groups and permissions created successfully"))

# python manage.py setup_groups



# can_crud_all model is created in postgres with codename, name, id & content_type_id columns
# in my case content_type_id is 7 as it is the id of blogpost model