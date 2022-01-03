from django.db import models
from django.utils.translation import gettext_lazy as _

from matches.models import Game
from players.models import Player


class Rally(models.Model):
    game = models.ForeignKey(
        Game,
        on_delete=models.CASCADE,
        related_name="rallies",
        verbose_name="Game",
    )
    rally_number = models.PositiveIntegerField(verbose_name="Rally Number")
    sequence = models.TextField(verbose_name="Sequence")
    service = models.ForeignKey(
        Player,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        verbose_name="Service",
    )
    winner = models.ForeignKey(
        Player,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        verbose_name="Winner",
    )
    loser = models.ForeignKey(
        Player,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        verbose_name="Loser",
    )

    class Meta:
        verbose_name = _("Rally")
        verbose_name_plural = _("Rallies")

    def __str__(self):
        return (
            f"Rally {self.rally_number} | {self.winner.name} - "
            f"{self.loser.name}"
        )
