from django.contrib import admin

# Register your models here.

from proposal.models import SpeechType, Topic, Speech


class SpeechAdmin(admin.ModelAdmin):
    list_display = ['user', 'title', 'skill_level']
    list_filter = ['topic', 'speech_type']

admin.site.register(Speech, SpeechAdmin)
admin.site.register([SpeechType, Topic])
