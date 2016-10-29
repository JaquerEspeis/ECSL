from datetime import datetime

from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls.base import reverse
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.utils.translation import ugettext_lazy as _
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.edit import CreateView, UpdateView

from register.forms import ProfileForm, InscriptionForm
from register.models import Profile, Inscription
from register.paypal import PaypalForm


def in_register_time():

    start_date = timezone.make_aware(
        datetime.strptime(settings.INSCRIPTION_START_DATE, '%d/%m/%Y %H:%M'),
        timezone.get_default_timezone())
    end_date = timezone.make_aware(datetime.strptime(
        settings.INSCRIPTION_END_DATE, '%d/%m/%Y %H:%M'),
        timezone.get_default_timezone())

    today = timezone.now()
    dev = False
    if start_date < today < end_date:
        dev = True
    return dev


@login_required
def subscribe(request):
    user = request.user
    success = None
    inscription = Inscription.objects.filter(user=user).first()
    if inscription and inscription.preregistered and in_register_time():
        form = PaypalForm(inscription)
        return render(request, 'register/inscription.html',
                      {'inscription': inscription,
                       'cost': settings.INSCRIPTION_COST,
                       'form': form})

    if request.method == 'POST':
        form = InscriptionForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = user
            instance.preregistered = True
            instance.save()
            success = _("Thanks, Inscription saved successfully ")
    else:
        form = InscriptionForm()
    return render(request, 'register/preinscription.html',
                  {'inscription': inscription,
                   'form': form,
                   'success': success})


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


@csrf_exempt
def paypal_response(request, status):
    return render(request, 'register/paypal.html', {'status': status})
