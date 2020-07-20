from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.db import models
from django.core.validators import RegexValidator
from django.utils.safestring import mark_safe
from django.utils import timezone
import datetime
from django.db import transaction
from rest_framework.authtoken.models import Token

#from notification_center.utils import SendNotification


USER_TYPE_CHOICES = (
        (1, 'Rider'),
        (2, 'Driver')
    )

class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, phone_number, password, **extra_fields):
        """Create and save a User with the given phone and password."""
        if not phone_number:
            raise ValueError('The given phone must be set')
        user = self.model(phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, phone_number, password=None, **extra_fields):
        """Create and save a regular User with the given phone and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(phone_number, password, **extra_fields)

    def create_superuser(self, phone_number, password, **extra_fields):
        """Create and save a SuperUser with the given phone and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(phone_number, password, **extra_fields)

class User(AbstractUser):
    """User model."""
    username = None
    first_name = models.CharField(max_length=254)
    last_name = models.CharField(max_length=254)
    phone_regex = RegexValidator(regex=r'^[6-9]\d{9}$', message="Phone number is not valid")
    phone_number = models.CharField(validators=[phone_regex], max_length=10, blank=False, unique=True)
    email = models.EmailField(_('email address'),blank=True)
    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES, default = '1', null=True)

    USERNAME_FIELD = 'phone_number'
    objects = UserManager()

    def __str__(self):
        return "%s - %s"%(str(self.phone_number), self.first_name)

