from django.db import models


from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin

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