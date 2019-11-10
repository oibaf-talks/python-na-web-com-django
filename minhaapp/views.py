from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView, UpdateView, DetailView

from minhaapp.forms import PresencaForm
from minhaapp.models import Presenca

# Create your views here.

def index(request):
    return HttpResponse('yey')

class ListaPresencaView(ListView):
    model = Presenca

class CriaPresencaView(CreateView):
    template_name = 'minhaapp/presenca.html'
    form_class = PresencaForm
    # success_url = reverse_lazy('presenca_list')
    success_url = '/minhaapp/list'


class EditPresencaView(UpdateView):
    template_name = 'minhaapp/presenca.html'
    model = Presenca
    fields = '__all__'
    # success_url = reverse_lazy('presenca_list')
    success_url = '/minhaapp/list'


class DeletePresencaView(DeleteView):
    model = Presenca
    # success_url = reverse_lazy('presenca_list')
    success_url = '/minhaapp/list'


class DetailPresencaView(DetailView):
    model = Presenca
