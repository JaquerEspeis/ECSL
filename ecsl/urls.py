"""ecsl URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from djreservation import urls as djreservation_urls

from hotel.urls import urlpatterns as hotel_urls
from imagen.views import index
from proposal.urls import urlpatterns as proposal_urls
from register.urls import urlpatterns as profile_urls
from tshirt.urls import urlpatterns as tshirt_urls


urlpatterns = [
    url(r'^$', index),
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('registration.backends.hmac.urls')),
    url(r'faq/', include('faq.urls')),
] + profile_urls + hotel_urls + tshirt_urls + djreservation_urls.urlpatterns\
    + proposal_urls
