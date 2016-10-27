from django.shortcuts import render

# Create your views here.

from djreservation.contrib.CRUD import UserObjectView
from proposal.models import Speech


class ProposalSpeech(UserObjectView):
    model = Speech
    template_name_base = "speech/speech"
    namespace = "speech"
    fields = [
        'speaker_information',
        'title',
        'topic',
        'description',
        'audience',
        'skill_level',
        'notes',
        'speech_type']

proposals = ProposalSpeech()
