from accounts.models import User
from rest_framework.permissions import BasePermission, IsAuthenticated
from django.core.exceptions import ObjectDoesNotExist

class IsAdminPermission(IsAuthenticated):
    def has_permission(self, request, view):
        is_authenticated = super().has_permission(request, view)
                
        if request.user.role == "admin" and is_authenticated:
            request.user.is_superuser = True
            request.user.save()
            return True
        else:
            return False
        

class IsTechnologist(IsAuthenticated):
    def has_permission(self, request, view):
        is_authenticated = super().has_permission(request, view)
        return request.user.role == "technologist" and is_authenticated


