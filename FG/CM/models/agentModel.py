from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager,
)


class CustomAccountManager(BaseUserManager):
    def create_superuser(
        self,
        username,
        first_name,
        last_name,
        password,
        **kwargs
    ):
        kwargs.setdefault('is_staff',True)
        kwargs.setdefault('is_superuser',True)
        kwargs.setdefault('is_active',True)
        kwargs.setdefault('role', Agent.Role.ADMIN)
        return self.create_user(username, first_name , last_name, password, **kwargs)

    def create_user(
        self,
        username,
        first_name,
        last_name,
        password,
        **kwargs
    ):
        if not username : 
            raise ValueError("You must provide a username")
        
        user = self.model(username = username, first_name = first_name, last_name = last_name, **kwargs)
        user.set_password(password)
        user.save()
        return user

class Agent(AbstractBaseUser, PermissionsMixin):
    class Role(models.TextChoices):
        ADMIN = "admin", ("Admin")
        CASHIER = "cashier", ("Cashier")
    username = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    cin = models.CharField(max_length=10)
    role = models.CharField(
        max_length=20, 
        choices=Role.choices,
        default=Role.CASHIER,
    )

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    objects = CustomAccountManager()

    USERNAME_FIELD = 'username'  # Field used as the unique identifier
    REQUIRED_FIELDS = ['first_name', 'last_name']  # Fields required for createsuperuser

    def __str__(self):
        return self.username