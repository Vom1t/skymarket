from django.contrib.auth.models import AbstractUser

from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from user.managers import UserManager


class UserRoles:

    USER = "user"
    ADMIN = "admin"
    choices = [
        ('user', 'Пользователь'),
        ('admin', 'Администратор'),
    ]


class User(AbstractUser):
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone', "role"]

    first_name = models.CharField(max_length=70,
                                  verbose_name='Имя')
    last_name = models.CharField(max_length=70,
                                 verbose_name='Фамилия')

    phone = PhoneNumberField(verbose_name='Телефонный номер')

    email = models.EmailField(verbose_name='E-mail',
                              unique=True)

    role = models.CharField(max_length=10,
                            choices=UserRoles.choices,
                            default="user",
                            verbose_name='Роль')

    image = models.ImageField(upload_to='images/user/',
                              null=True,
                              blank=True)

    @property
    def is_superuser(self):
        return self.is_admin

    @property
    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin

    @property
    def is_admin(self):
        return self.role == UserRoles.USER

    @property
    def is_user(self):
        return self.role == UserRoles.ADMIN

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ["id"]


