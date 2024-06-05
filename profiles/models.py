from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    A model representing a user profile.

    Attributes:
        user (OneToOneField): The associated user for the profile.
        favorite_city (CharField): The user's favorite city (up to 64 characters, optional).

    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self):
        return self.user.username
