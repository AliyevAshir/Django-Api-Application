from rest_framework.permissions import BasePermission

class IsAdminOrReadOnly(BasePermission):
    """
    Custom permission to only allow authenticated users for GET, POST, and PUT methods,
    and only allow admin users for DELETE method.
    """
    def has_permission(self, request, view):
        # Allow all users to access GET methods
        if request.method == 'GET':
            return True
        # Allow authenticated users for POST and PUT methods
        elif request.method in ['POST', 'PUT']:
            return request.user and request.user.is_authenticated
        # Only allow admin users for DELETE method
        elif request.method == 'DELETE':
            return request.user and request.user.is_authenticated and request.user.is_staff
        return False
