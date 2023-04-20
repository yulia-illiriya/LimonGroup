from accounts.models import User
from rest_framework.permissions import BasePermission, IsAuthenticated
from django.core.exceptions import ObjectDoesNotExist


class IsAdminPermission(IsAuthenticated):
    def has_permission(self, request, view):
        is_authenticated = super().has_permission(request, view)
<<<<<<< HEAD

        try:
            admin = request.user.role.admin
        except User.role.RelatedObjectDoesNotExist:
            return False

        if admin and is_authenticated:
=======
                
        if request.user.role == "admin" and is_authenticated:
>>>>>>> d7e662280d5a1e8f8e03b075cf6286a2cfd745b3
            request.user.is_superuser = True
            request.user.save()
            return True
        else:
            return False
<<<<<<< HEAD
=======
        

class IsTechnologist(IsAuthenticated):
    def has_permission(self, request, view):
        is_authenticated = super().has_permission(request, view)
        return request.user.role == "technologist" and is_authenticated


>>>>>>> d7e662280d5a1e8f8e03b075cf6286a2cfd745b3
