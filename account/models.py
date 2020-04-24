from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# Create your models here.

class MyAccountManager(BaseUserManager):
    def create_user(self, username, first_name, password=None):
        if not username:
            raise ValueError("Need username!")
        if not first_name:
            raise ValueError("Need Name (first name)")

        user = self.model(
            username=username,
            first_name=first_name,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, first_name, password):
        user = self.create_user(
            username=username,
            first_name=first_name,
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    id = models.AutoField(verbose_name="ID", primary_key=True, auto_created=True, serialize=False)
    username = models.CharField(verbose_name="Login", max_length=50, unique=True)
    date_joined = models.DateTimeField(verbose_name="Date joined", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="Last login date", auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    first_name = models.CharField(verbose_name="Name", max_length=50)
    chat_id = models.TextField(verbose_name="TG Chat ID", default=None, null=True, blank=True)
    token = models.TextField(verbose_name="Access token", default=None, null=True, blank=True)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ['first_name']

    objects = MyAccountManager()

    def __str__(self):
        return self.username + ", " + self.first_name

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_Label):
        return True