from django.db import models

from django.contrib.auth.base_user import AbstractBaseUser
from django.core.validators import RegexValidator
from django.contrib.auth.models import PermissionsMixin

from accounts.managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    ROLE_CHOICES = (
        ('admin', 'Администратор'),
        ('purchaser', 'Закупщик'),
        ('sales_manager', 'Менеджер по продажам'),
        ('technologist', 'Технолог'),
        ('accountant', 'Бухгалтер'),
        ('assistent', 'Ассистент')
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)    
    email = models.EmailField(
        verbose_name="Email",
        max_length=255,
        unique=True,
    )
    username = models.CharField(max_length=255, verbose_name='Имя', unique=True)
    date_created = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=True)

    objects = UserManager()

    USERNAME_FIELD = "username"

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

