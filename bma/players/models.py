from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from players.constants import Country, Handedness


class Player(models.Model):
    name = models.CharField(max_length=64, verbose_name="Name")
    age = models.PositiveIntegerField(verbose_name="Age")
    country = models.CharField(
        max_length=2, choices=Country.choices, verbose_name="Country"
    )
    handedness = models.CharField(
        max_length=1, choices=Handedness.choices, verbose_name="Handedness"
    )
    height = models.PositiveIntegerField(verbose_name="Height (cm)")
    professional = models.BooleanField(
        default=False, verbose_name="Professional"
    )
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = _("Player")
        verbose_name_plural = _("Players")

    def __str__(self):
        return self.name
