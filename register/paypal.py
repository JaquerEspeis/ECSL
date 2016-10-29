# encoding: utf-8


'''
Created on 28/10/2016

@author: luisza
'''
from __future__ import unicode_literals
from django.conf import settings
from django.urls.base import reverse
from paypal.standard.forms import PayPalPaymentsForm


def PaypalForm(inscription):

    paypal_dict = {
        "business": settings.PAYPAL_EMAIL,
        "amount": settings.INSCRIPTION_COST + ".00",
        "item_name": "ECSL de " + inscription.user.get_full_name(),
        "invoice": "ecsl_%d" % (inscription.pk, ),
        "notify_url": settings.PAYPAL_SITE_BASE + reverse('paypal-ipn'),
        "return_url": settings.PAYPAL_SITE_BASE + reverse("paypal_ap",
                                                          args=("success",)),
        "cancel_return": settings.PAYPAL_SITE_BASE + reverse("paypal_ap",
                                                             args=("wrong",)),
        # Custom command to correlate to some function later (optional)
        #"custom": "Upgrade all users!",
    }

    # Create the instance.
    form = PayPalPaymentsForm(initial=paypal_dict)

    return form
