from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator
from django.utils.translation import gettext_lazy as _


class Address(models.Model):
    """
    A model to represent a physical address.

    Attributes:
        number (PositiveIntegerField): The street number of the address (up to 9999).
        street (CharField): The street name (up to 64 characters).
        city (CharField): The city name (up to 64 characters).
        state (CharField): The state abbreviation (2 characters, e.g., 'CA' for California).
        zip_code (PositiveIntegerField): The ZIP code (up to 99999).
        country_iso_code (CharField): The ISO country code.
    """
    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
    country_iso_code = models.CharField(max_length=3, validators=[MinLengthValidator(3)])

    class Meta:
        verbose_name = _("Address")
        verbose_name_plural = _("Addresses")

    def __str__(self):
        return f'{self.number} {self.street}'


class Letting(models.Model):
    """
    A model representing a letting property.

    Attributes:
        title (CharField): The title or name of the letting (up to 256 characters).
        address (OneToOneField): The address associated with the letting.
    """
    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
