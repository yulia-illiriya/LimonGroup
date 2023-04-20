from accounts.models import User
from rest_framework.permissions import BasePermission, IsAuthenticated

class IsAdminPermission(IsAuthenticated):
    def has_permission(self, request, view):
        is_authenticated = super().has_permission(request, view)
        
        try:
            admin = request.user.role.admin
        except User.role.RelatedObjectDoesNotExist:
            return False
        
        if admin and is_authenticated:
            request.user.is_superuser = True
            request.user.save()
            return True
        else:
            return False


