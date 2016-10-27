'''
Created on Oct 4, 2016

@author: usuario
'''

from djreservation.views import SimpleProductReservation
from hotel.models import Room


class RoomReservation(SimpleProductReservation):
    base_model = Room     # required
    amount_field = 'available_beds'  # required
    extra_display_field = []  # not required
    max_amount_field = 'available_beds'
