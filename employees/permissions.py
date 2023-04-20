from rest_framework.permissions import SAFE_METHODS, BasePermission
from accounts.permissions import IsAdminPermission

class IsAdminOrReadOnly(IsAdminPermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        else:
            return super().has_permission(request, view)