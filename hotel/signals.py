# encoding: utf-8

'''
Free as freedom will be 5/10/2016

@author: luisza
'''

from __future__ import unicode_literals

from django.conf import settings
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.loader import render_to_string
from djreservation.models import ReservationToken


@receiver(post_save, sender=ReservationToken)
def send_token(sender, **kwargs):
    token = kwargs['instance']
    reservation = token.reservation
    product = reservation.product_set.all()[0]
    hotel = product.content_object.hotel

    send_mail(
        '[ECSL] Nueva reservación',
        'Por favor use un visor con soporte a html',
        settings.DEFAULT_FROM_EMAIL,
        [hotel.contact_email],
        html_message=render_to_string(
            'mail/hotel_admin.html',
            {
                'reservation': reservation,
                'product': product,
                'hotel': hotel,
                'perfil': reservation.user.perfil,
                'token': token
            }
        ),
        fail_silently=False,
    )
