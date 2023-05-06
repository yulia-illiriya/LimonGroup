from django.db import models
from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, role, username, password=None):
        if not email:
            raise ValueError("Users must have email address")
        if not role:
            raise ValueError("Users must have role")

        email = self.normalize_email(email)
        user = self.model(
            email=email,
            username=username,
            role=role
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None):

        user = self.create_user(
            email=email,
            password=password,
            username=username,
            role='admin'
        )
        user.set_password(password)
        user.is_admin = True
        user.is_superuser = True
        user.save()

        print(user.role)

        return user
