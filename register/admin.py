from django.contrib import admin

from register.models import Profile, Inscription

admin.site.register([Profile, Inscription])