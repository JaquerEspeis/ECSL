
from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _


# Create your models here.
class TShirtStyle(models.Model):
    name = models.CharField(max_length=150, verbose_name=_("Name"))
    gender = models.CharField(
        max_length=1, choices=(('M', _('Women')), ('H', _('Man'))),
        verbose_name=_("Gender")
    )
    description = models.TextField(verbose_name=_("Description"))
    price = models.DecimalField(max_digits=12, decimal_places=2,
                                verbose_name=_("Price"))

    img1 = models.ImageField(upload_to="tshirt/%Y/", null=True, blank=True)
    img2 = models.ImageField(upload_to="tshirt/%Y/", null=True, blank=True)
    img3 = models.ImageField(upload_to="tshirt/%Y/", null=True, blank=True)

    def __str__(self):
        return _("%s of %s", self.nombre,  self.get_genero_display())


class Tshirt(models.Model):
    SIZE = (
        ('XS', 'XS'), ('S', 'S'),
        ('XM', 'XM'), ('M', 'M'),
        ('L', 'L'), ('XL', 'XL'),
        ('XXL', 'XXL'),)
    user = models.ForeignKey(User, verbose_name=_("User"))
    size = models.CharField(max_length=3, choices=SIZE, verbose_name=_("Size"))
    style = models.ForeignKey(TShirtStyle, verbose_name=_("Style"))
    amount = models.PositiveIntegerField(default=1, verbose_name=_("Amount"))
    last_update = models.DateTimeField(
        auto_now=True, verbose_name=_("Last Update"))

    def __str__(self):
        return _("Cantidad: %d talla: %s tipo: %s", self.amount, self.size, self.style)
