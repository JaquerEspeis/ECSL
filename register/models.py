
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
    snore = models.BooleanField(default=False,
                                verbose_name=_("Snore during sleep"))
    alimentary_restriction = models.TextField(
        null=True, blank=True,
        verbose_name=_("Alimentary restriction"))

    health_considerations = models.TextField(
        null=True, blank=True,
        verbose_name=_("Health considerations"))


class Inscription(models.Model):
    user = models.OneToOneField(User)
    preregistered = models.BooleanField(default=False,
                                        verbose_name=_("Pre-registered")
                                        )
    registered = models.BooleanField(default=False,
                                     verbose_name=_("Registered")
                                     )

    mozilla_subvention = models.BooleanField(default=False,
                                             verbose_name=_(
                                                 "Mozilla Subvention")
                                             )

    mozilla_subvention_description = models.TextField(
        null=True, blank=True,
        verbose_name=_("Why should we give you the mozilla subvention")
    )
    subvention_request = models.BooleanField(default=False,
                                             verbose_name=_(
                                                 "Subvention request")
                                             )
    subvention_description = models.TextField(
        null=True, blank=True,
        verbose_name=_("Why should we give you the subvention")
    )
    payed = models.BooleanField(default=False,
                                verbose_name=_("Payed")
                                )

    def __str__(self):
        return self.user.get_full_name()
