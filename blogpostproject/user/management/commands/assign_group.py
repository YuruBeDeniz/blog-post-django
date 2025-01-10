from django.core.management.base import BaseCommand
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group

class Command(BaseCommand):
    help = 'Assign a user to a group'

    def add_arguments(self, parser):
        parser.add_argument('username', type=str, help="The username of the user")
        parser.add_argument('group', type=str, help="The group to assign the user to")

    def handle(self, *args, **kwargs):
        username = kwargs['username']
        group_name = kwargs['group']

        User = get_user_model()  # Get the custom User model
        try:
            user = User.objects.get(username=username)
            group = Group.objects.get(name=group_name)
            user.groups.add(group)
            self.stdout.write(self.style.SUCCESS(f"User '{username}' added to group '{group_name}'"))
        except User.DoesNotExist:
            self.stderr.write(self.style.ERROR(f"User '{username}' does not exist"))
        except Group.DoesNotExist:
            self.stderr.write(self.style.ERROR(f"Group '{group_name}' does not exist"))



# python manage.py assign_group <username> <group>

# python manage.py makemigrations && migrate
