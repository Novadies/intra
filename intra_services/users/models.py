from ckeditor_uploader.fields import RichTextUploadingField

from django.contrib.auth.hashers import check_password, make_password
from django.contrib.auth.models import AbstractUser, UserManager
from django.contrib.auth.password_validation import validate_password
from django.core.validators import MinLengthValidator
from django.db import models
from django.db.models import Q


class CustomUserManager(UserManager):
    """ кастомный юзер. Cоздан метод на основе get_by_natural_key"""
    def get_by_natural_key_v2(self, username):
        """ используется кастомный ALL_USERNAME_FIELD """
        all_fields = getattr(self.model, "ALL_USERNAME_FIELD", None)
        if all_fields is not None:
            conditions = Q()
            for field in all_fields:
                conditions |= Q(**{field: username})
            return self.get(conditions)
        else:
            return self.get_by_natural_key(username)


class User(AbstractUser):
    """ дополнение базового юзера """
    objects = CustomUserManager()
    email = models.EmailField(unique=True, null=True)


    REQUIRED_FIELDS = ['username']  # обязательные поля
    USERNAME_FIELD = 'email'  # вместо логина
    ALL_USERNAME_FIELD = 'email', 'username' # это кастомная константа, имеет приоритет перед USERNAME_FIELD

    def __str__(self):
        return self.first_name or self.username

    def save(self, *args, **kwargs):
        """ Иначе email будут пустыми, что выкинет ошибку """
        fields_to_check = ['email']
        for field in fields_to_check:
            if getattr(self, field) == "":
                setattr(self, field, None)
        super().save(*args, **kwargs)


class UserExtraField(models.Model):
    """ расширение модели юзера """
    votes = models.IntegerField(default=0)
    photo = models.ImageField(upload_to="users/%Y/%m/%d/", blank=True, null=True, verbose_name="Фотография")
    date_birth = models.DateTimeField(blank=True, null=True, verbose_name="Дата рождения")
    about_user = RichTextUploadingField(blank=True)

    to_user = models.OneToOneField(
        "User",
        primary_key=True,                   # to_user будет ключом
        on_delete=models.CASCADE,
        unique=True,
        related_name="user_extra_field",
    )

    def __str__(self):
        return f'{self.to_user}'
