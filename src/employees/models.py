from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Employee(MPTTModel):

    POSITION_CHOICES = (
        ("position_1", "position_1"),
        ("position_2", "position_2"),
        ("position_3", "position_3"),
        ("position_4", "position_4"),
        ("position_5", "position_5"),
        ("position_6", "position_6"),
        ("position_7", "position_7"),
        ("position_8", "position_8"),
    )

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

    class MPTTMeta:
        parent_attr = "boss"
        order_insertion_by = ["last_name"]
