from django.db import models
from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **kwargs):
        if not email:
            raise ValueError("Users must have email address")
        if not kwargs.get('role'):
            raise ValueError("Users must have role")
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            username=kwargs.get('username'),
            role=kwargs.get('role')
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None, **kwargs):
        kwargs.setdefault('is_superuser', True)
        kwargs.setdefault('is_admin', True)
        kwargs.setdefault('is_active', True)
        # kwargs.setdefault('is_staff', True)
        kwargs.setdefault('role', 'admin')

        if not email:
            raise ValueError("Users must have email address")
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            username=kwargs.get('username'),
            role=kwargs.get('role')
        )
        user.set_password(password)
        user.save()
        return user
