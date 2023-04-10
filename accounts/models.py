from django.db import models

from django.contrib.auth.base_user import AbstractBaseUser
from django.core.validators import RegexValidator
from django.contrib.auth.models import PermissionsMixin

from accounts.managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    POSITION_CHOICES = (
        ('Administrator', 'Administrator'),
        ('Technologist', 'Technologist'),
        ('Zakroi', 'Zakroi')
    )

    position = models.CharField(max_length=50, choices=POSITION_CHOICES)
    email = models.EmailField(
        verbose_name="Email",
        max_length=255,
        unique=True,
    )
    first_name = models.CharField(max_length=255, verbose_name='Имя')
    last_name = models.CharField(max_length=255, verbose_name='Фамилия')
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)
    phone_number = models.CharField(
        validators=[RegexValidator(
            regex='^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$',
            message='phone number must be digits',
            code='invalid phone number'
        )],
        max_length=15,
        verbose_name='Контакты'
    )
    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    def str(self):
        return self.email

    def has_module_perms(self, app_label):
        return self.is_superuser

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
