from django.db import models
from django.utils.translation import gettext_lazy as _


class Country(models.TextChoices):
    CANADA = "CA", _("Canada")
    CHINA = "CN", _("China")
    DENMARK = "DK", _("Denmark")
    ENGLAND = "UK", _("England")
    FRANCE = "FR", _("France")
    GERMANY = "DE", _("Germany")
    HONG_KONG = "HK", _("Hong Kong")
    INDIA = "IN", _("India")
    INDONESIA = "ID", _("Indonesia")
    JAPAN = "JP", _("Japan")
    KOREA = "KR", _("Korea")
    MALAYSIA = "MY", _("Malaysia")
    RUSSIA = "RU", _("Russia")
    SINGAPORE = "SG", _("Singapore")
    SPAIN = "ES", _("Spain")
    TAIWAN = "TW", _("Taiwan")
    THAILAND = "TH", _("Thailand")
    VIETNAM = "VN", _("Vietnam")


class Handedness(models.TextChoices):
    LEFT = "L", _("Left")
    RIGHT = "R", _("Right")
