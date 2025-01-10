from rest_framework.permissions import BasePermission
from rest_framework import permissions

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
        return request.method in permissions.SAFE_METHODS

class IsAuthorOrAdmin(BasePermission):
    """
    Allows authors to edit/delete their own posts and admins to access all.
    """
    def has_object_permission(self, request, view, obj):
        is_admin = request.user.groups.filter(name='Admin').exists()
        return obj.author == request.user or is_admin
    
    
# As well as global permissions, that are run against all incoming requests, 
# you can also create object-level permissions, that are only run against operations 
# that affect a particular object instance


# BasePermission methods:
# .has_permission(self, request, view): When the permission applies to the entire view or endpoint.
# .has_object_permission(self, request, view, obj): When the permission applies to a specific object instance.
# The methods should return True if the request should be granted access, 
# and False otherwise.

# IsAdminUserOrReadOnly:
# Focuses on the method type (GET vs. POST/PUT/DELETE) and checks at the view level.
# IsAuthorOrAdmin:
# Focuses on permissions for specific objects (e.g., whether a user is allowed to update or delete a particular post).

