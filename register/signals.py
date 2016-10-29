# encoding: utf-8


'''
Created on 28/10/2016

@author: luisza
'''
from __future__ import unicode_literals

from django.conf import settings
from paypal.standard.ipn.signals import valid_ipn_received
from paypal.standard.models import ST_PP_COMPLETED
from register.models import Inscription


def subscription_success(sender, **kwargs):
    ipn_obj = sender
    if ipn_obj.payment_status == ST_PP_COMPLETED:
        # WARNING !
        # Check that the receiver email is the same we previously
        # set on the business field request. (The user could tamper
        # with those fields on payment form before send it to PayPal)
        if ipn_obj.receiver_email != settings.PAYPAL_EMAIL:
            # Not a valid payment
            return

        # ALSO: for the same reason, you need to check the amount
        # received etc. are all what you expect.

        # Undertake some action depending upon `ipn_obj`.

        pk = ipn_obj.invoice.replace('ecsl_', '')
        inscription = Inscription.objects.filter(pk=pk).first()
        if inscription:
            inscription.payed = True
            inscription.save()
valid_ipn_received.connect(subscription_success)
