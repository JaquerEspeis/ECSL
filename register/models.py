
from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.
# Create your models here.


class Profile(models.Model):
    NACIONALITIES = (
        ('PA', "Panamá"),
        ('CR', "Costa Rica"),
        ('NI', "Nicaragua"),
        ('HON', "Honduras"),
        ("SAL", "Salvador"),
        ("BEL", "Belice"),
        ("GUA", "Guatemala"),
        ("otro", _("Other nacionalities"))

    )
    GENDER = (
        (0, _('Male')),
        (1, _('Female')),
        (2, _("Other")),
    )

    user = models.OneToOneField(User,
                                verbose_name=_("User"))
    nacionality = models.CharField(
        max_length=5,
        choices=NACIONALITIES,
        verbose_name=_("Nacionality"))

    identification = models.CharField(max_length=20,
                                      verbose_name=_("Identification"))
    born_date = models.DateField(verbose_name=_("Born date"))
    gender = models.SmallIntegerField(
        choices=GENDER,
        verbose_name=_("Gender")
    )
    institution = models.CharField(max_length=250, null=True,
                                   blank=True,
                                   verbose_name=_("Institution"))
