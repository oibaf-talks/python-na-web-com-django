from django.http import HttpResponse
from django.shortcuts import render
# from django.urls import reverse_lazy
from django.views.generic import FormView

from minhaapp.forms import PresencaForm

# Create your views here.

def index(request):
    return HttpResponse('yey')

class ContactView(FormView):
    template_name = 'minhaapp/presenca.html'
    form_class = PresencaForm
    # success_url = reverse_lazy('site.index')
    success_url = '/'
