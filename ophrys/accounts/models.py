from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager, Group,
                                        PermissionsMixin)
from django.db import models
from django.utils import timezone

from ophrys.utils.models import GetAbsoluteUrlMixin


class UserManager(PermissionsMixin, BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        now = timezone.now()
        if not email:
            raise ValueError('The given email must be set.')
        email = UserManager.normalize_email(email)
        user = self.model(email=email, last_login=now,
                          **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, is_superuser=True, **extra_fields):
        return self.create_user(email, password, is_superuser=is_superuser,
                                **extra_fields)


class User(GetAbsoluteUrlMixin, AbstractBaseUser):
    email = models.EmailField(max_length=254, unique=True, db_index=True)
    is_active = models.BooleanField(default=True)  # blank=True
    date_joined = models.DateTimeField(auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def get_full_name(self):
        return 'Full: %s' % self.email

    def get_short_name(self):
        return 'Short: %s' % self.email
