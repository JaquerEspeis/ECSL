from decimal import Decimal

from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.


class Hotel(models.Model):
    name = models.CharField(max_length=250,
                            verbose_name=_("Name"))
    description = models.TextField(verbose_name=_("Description"))
    url = models.URLField(verbose_name=_("Url"))
    contact_email = models.EmailField(default="changeme@example.com",
                                      verbose_name=_("Contact email"))

    def __str__(self):
        return self.name

    def get_room_per_floor(self):
        rooms_set = self.room_set.all().order_by('floor')
        rooms = []
        lfloor = None
        for room in rooms_set:
            if lfloor is None:
                rooms.append(room)
                lfloor = room.floor
                continue
            if lfloor != room.floor:
                yield rooms
                rooms = []
                lfloor = room.floor

            rooms.append(room)
        if rooms:
            yield rooms


class Room(models.Model):
    FLOORS = (
        (1, _('First floor')),
        (2, _('Second floor')),
        (3, _('Third floor')),
        (4, _('Fourth floor')),
        (5, _('Fifth floor')),
    )
    hotel = models.ForeignKey(Hotel, verbose_name=_("Hotel"))
    floor = models.SmallIntegerField(choices=FLOORS, default=1,
                                     verbose_name=_("Floor"))
    number = models.CharField(max_length=15, verbose_name=_("Number"))
    total_beds = models.SmallIntegerField(
        default=1, verbose_name=_("Total beds"))
    matrimonial = models.BooleanField(default=False,
                                      verbose_name=_("Matrimonial"))
    available_beds = models.SmallIntegerField(default=0,
                                              verbose_name=_("Available beds"))
    price_per_bed = models.DecimalField(max_digits=10, decimal_places=2,
                                        default=Decimal(0.0),
                                        verbose_name=_("Price per bed"))
    coin = models.CharField(max_length=10, default="$",
                            verbose_name=_("Pay in "))

    def __str__(self):
        return _("%s floor %d, room %s %s %.3f", self.hotel,
                 self.floor,
                 self.number,
                 self.coin,
                 self.price_per_bed)
