from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

from .managers import EmployeeManager
from .utils import POSITION_CHOICES


class Employee(MPTTModel):

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    email = models.EmailField()

    employment_at = models.DateField()

    position = models.CharField(choices=POSITION_CHOICES, max_length=20)

    boss = TreeForeignKey(
        "self",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="workmates",
    )

    objects = EmployeeManager()

    class MPTTMeta:
        parent_attr = "boss"
        ordering = ["last_name"]
        order_insertion_by = ["last_name"]
