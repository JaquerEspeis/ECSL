from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class TshirtConfig(AppConfig):
    name = 'tshirt'
    verbose_name = _("TShirt")
    verbose_name_plural = _("TShirts")
