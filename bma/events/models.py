from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _


class EventCategory(models.Model):
    name = models.CharField(max_length=128, verbose_name="Name")
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = _("Event Category")
        verbose_name_plural = _("Event Categories")

    def __str__(self):
        return self.name


class Event(models.Model):
    name = models.CharField(max_length=128, verbose_name="Name")
    category = models.ForeignKey(
        EventCategory,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name="events",
        verbose_name="Event Category",
    )
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = _("Event")
        verbose_name_plural = _("Events")

    def __str__(self):
        return self.name
