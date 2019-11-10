from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from minhaapp.forms import PresencaForm
from minhaapp.models import Presenca

# Create your views here.

def index(request):
    return HttpResponse('yey')

class ListaPresencaView(ListView):
    model = Presenca

class PresencaView(CreateView):
    template_name = 'minhaapp/presenca.html'
    form_class = PresencaForm
    # success_url = reverse_lazy('presenca_list')
    success_url = '/minhaapp/list'
