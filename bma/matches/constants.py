from django.db import models
from django.utils.translation import gettext_lazy as _


class Discipline(models.TextChoices):
    MD = "MD", _("MD")
    MS = "MS", _("MS")
    WD = "WD", _("WD")
    WS = "WS", _("WS")
    XD = "XD", _("XD")
