from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError



class User(AbstractUser):
    ROLE_CHOICES = [
        ("Admin", "Admin"),
        ("Student", "Student"),
    ]

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    last_login = models.DateTimeField(auto_now=True)


    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default="Student", blank=True)

    def __str__(self) -> str:
        return f"{self.username} - {self.role}"

    groups = models.ManyToManyField(
        "auth.Group",
        verbose_name="groups",
        blank=True,
        related_name="custom_user_set",  # Change related_name
        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        verbose_name="user permissions",
        blank=True,
        related_name="custom_user_set",  # Change related_name
        help_text="Specific permissions for this user.",
    )
