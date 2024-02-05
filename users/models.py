from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class UserRoles(models.TextChoices):
    MEMBER = 'member'
    MODERATOR = 'moderator'


class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True, verbose_name='Почта')

    phone = models.CharField(max_length=25, **NULLABLE, verbose_name='Телефон')
    city = models.CharField(max_length=100, **NULLABLE, verbose_name='Город')
    avatar = models.ImageField(upload_to='users/', **NULLABLE, verbose_name='Аватар')
    role = models.CharField(max_length=9, choices=UserRoles.choices, verbose_name='Роль', default=UserRoles.MEMBER)
    is_active = models.BooleanField(default=False, verbose_name='Активность')
    last_login = models.DateField(verbose_name='Последний вход', default='2024-01-01', )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
