'''
Created on Oct 2, 2016

@author: usuario
'''
from django.conf.urls import url, include

from register.views import UpdateProfile, CreateProfile, profile_view, subscribe,\
    paypal_response

urlpatterns = [
    url(r'accounts/profile/?$', profile_view, name="profile"),
    url(r'^register/profile/create$',
        CreateProfile.as_view(), name='create_profile'),
    url(r'^register/profile/update/(?P<pk>\d+)$',  UpdateProfile.as_view(),
        name='edit_profile'),
    url(r'^register/subscribeme$', subscribe, name="subscribe"),
    url(r'register/paypal/(?P<status>\w+)$',
        paypal_response, name="paypal_ap"),
    url(r'^\/?paypal/', include('paypal.standard.ipn.urls')),
]
