from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls.base import reverse
from django.utils.decorators import method_decorator
from django.utils.translation import ugettext_lazy as _
from django.views.generic.edit import CreateView, UpdateView

from register.forms import ProfileForm
from register.models import Profile


@method_decorator(login_required, name='dispatch')
class CreateProfile(CreateView):
    model = Profile
    form_class = ProfileForm

    success_url = "/"

    def form_valid(self, form):
        messages.success(self.request, _('Profile created successfully'))
        form.instance.user = self.request.user
        user = self.request.user
        user.first_name = form.cleaned_data['first_name']
        user.last_name = form.cleaned_data['last_name']
        user.save()
        return super(CreateProfile, self).form_valid(form)

    def get(self, request, *args, **kwargs):
        profile = self.model.objects.filter(user=request.user)
        if len(profile):
            return redirect(reverse('edit_profile', args=(profile[0].pk,)))
        return super(CreateProfile, self).get(self, request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        profile = self.model.objects.filter(user=request.user)
        if len(profile):
            return redirect(reverse('edit_profile', args=(profile[0].pk,)))
        return CreateView.post(self, request, *args, **kwargs)


@method_decorator(login_required, name='dispatch')
class UpdateProfile(UpdateView):
    model = Profile
    form_class = ProfileForm
    success_url = "/"

    def form_valid(self, form):
        messages.success(self.request, _('Profile updated successfully'))
        return UpdateView.form_valid(self, form)


# Create your views here.
@login_required
def profile_view(request):
    try:
        profile = Profile.objects.get(user=request.user)
        return redirect(reverse('edit_profile', args=(profile.pk,)))
    except:
        return redirect(reverse('create_profile'))
