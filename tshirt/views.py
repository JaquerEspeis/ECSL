from django.shortcuts import render

# Create your views here.

from djreservation.contrib.CRUD import UserObjectView
from tshirt.models import Tshirt


class TShirtView(UserObjectView):
    model = Tshirt  # requiered
    template_name_base = "tshirt/tshirt"  # not required but recomendable
    namespace = "tshirt"  # required
    fields = ['size', 'style', 'amount']  # not required

tshirts = TShirtView()
