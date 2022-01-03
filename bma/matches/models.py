from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from events.models import Event
from matches.constants import Discipline
from players.models import Player


class Match(models.Model):
    event = models.ForeignKey(
        Event,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="matches",
        verbose_name="Match",
    )
    discipline = models.CharField(
        max_length=2, choices=Discipline.choices, verbose_name="Discipline"
    )
    winner = models.ForeignKey(
        Player,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="won_matches",
        verbose_name="Winner",
    )
    loser = models.ForeignKey(
        Player,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="lost_matches",
        verbose_name="Loser",
    )
    date = models.DateField(verbose_name="Date")
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = _("Match")
        verbose_name_plural = _("Matches")

    def __str__(self):
        return f"Match | {self.winner} - {self.loser} | {self.date}"


class Game(models.Model):
    event = models.ForeignKey(
        Event,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="games",
        verbose_name="Game",
    )
    game_number = models.PositiveIntegerField(verbose_name="Game Number")
    discipline = models.CharField(
        max_length=2, choices=Discipline.choices, verbose_name="Discipline"
    )
    winner = models.ForeignKey(
        Player,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="won_games",
        verbose_name="Winner",
    )
    loser = models.ForeignKey(
        Player,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="lost_games",
        verbose_name="Loser",
    )
    winner_score = models.PositiveIntegerField(verbose_name="Winner Score")
    loser_score = models.PositiveIntegerField(verbose_name="Loser Score")
    date = models.DateField(verbose_name="Date")
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = _("Game")
        verbose_name_plural = _("Games")

    def __str__(self):
        return f"Game | {self.winner} - {self.loser} | {self.date}"
