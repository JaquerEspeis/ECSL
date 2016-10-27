# encoding: utf-8

'''
Free as freedom will be 4/10/2016

@author: luisza
'''

from __future__ import unicode_literals
from django.views.generic.list import ListView
from hotel.models import Hotel


class HotelList(ListView):
    model = Hotel
