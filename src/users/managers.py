from django.contrib.auth.models import BaseUserManager, PermissionsMixin


class CustomManager(BaseUserManager, PermissionsMixin): ...
