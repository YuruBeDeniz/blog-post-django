from rest_framework.permissions import BasePermission

class IsAdminUserOrReadOnly(BasePermission):
    """
    Allows full access to Admin group members. Authenticated users can perform non-destructive actions.
    """
    def has_permission(self, request, view):
        if request.user.is_authenticated and request.method in ['POST', 'PUT', 'DELETE']:
            if request.user.groups.filter(name='Admin').exists():
                return True
            # Non-admins are restricted to GET, HEAD, and OPTIONS
            return False
        return request.method in ['GET', 'HEAD', 'OPTIONS']

class IsAuthorOrAdmin(BasePermission):
    """
    Allows authors to edit/delete their own posts and admins to access all.
    """
    def has_object_permission(self, request, view, obj):
        is_admin = request.user.groups.filter(name='Admin').exists()
        return obj.author == request.user or is_admin
