from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.contrib.auth.hashers import make_password
from phonenumber_field import modelfields
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import RegexValidator

NULLABLE = {'blank': True, 'null': True}


class CustomUserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    def create_superuser(self, phone, password=None, **extra_fields):
        """Create and save a SuperUser with the given phone and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(phone, password, **extra_fields)

    def _create_user(self, phone, password, **extra_fields):
        """Create and save a User with the given phone and password."""
        if not phone:
            raise ValueError('The given phone must be set')
        user = self.model(phone=phone, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    # def _create_user(self, phone, password, **extra_fields):
    #     extra_fields.setdefault('is_staff', False)
    #     extra_fields.setdefault('is_superuser', False)
    #     return self._create_user(phone, password, **extra_fields)


class User(AbstractUser):
    username = None
    phone = models.CharField(verbose_name='Номер телефона', max_length=5000, unique=True, db_index=True)
    # phone = modelfields.PhoneNumberField(unique = True, null = False, blank = False, validators=[RegexValidator(r'^\d{3}-\d{3}-\d{4}$')], region="US").as_e164
    new_password = models.CharField(max_length=200, verbose_name="новый пароль", **NULLABLE)

    USERNAME_FIELD = "phone"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return str(self.phone)

