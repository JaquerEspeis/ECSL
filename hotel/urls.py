# encoding: utf-8

'''
Free as freedom will be 27/10/2016

@author: luisza
'''

from __future__ import unicode_literals

from django.conf.urls import url

from hotel.HotelView import HotelList
from hotel.reservations import RoomReservation


urlpatterns = [
    url(r"^hotel$", HotelList.as_view(), name="hotel_list"),
    url(r"^roomreservation/create/(?P<pk>\d+)$", RoomReservation.as_view(),
        name="reserve_room"),
]
