# encoding: utf-8

'''
Free as freedom will be 5/10/2016

@author: luisza
'''

from __future__ import unicode_literals

from django import forms
from django.utils.translation import ugettext_lazy as _

from register.models import Profile, Inscription


class ProfileForm(forms.ModelForm):
    first_name = forms.CharField(label=_("First name"))
    last_name = forms.CharField(label=_("Last name"))

    field_order = [
        'first_name', 'last_name',
        'identification', 'nacionalidad',
        'born_date', 'gender', 'institution'
    ]

    def __init__(self, *args, **kwargs):
        if 'instance' in kwargs and kwargs['instance']:
            perfil = kwargs['instance']
            kwargs['initial']['first_name'] = perfil.user.first_name
            kwargs['initial']['last_name'] = perfil.user.last_name

        super(ProfileForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        dev = super(ProfileForm, self).save(commit=commit)

        if self.instance:
            user = self.instance.user
            user.first_name = self.cleaned_data['first_name']
            user.last_name = self.cleaned_data['last_name']
            user.save()
        return dev

    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ['user']


class InscriptionForm(forms.ModelForm):

    class Meta:
        model = Inscription
        fields = ['subvention_request', 'subvention_description',
                  'mozilla_subvention', 'mozilla_subvention_description'
                  ]
