from django.forms import ModelForm

from minhaapp import models


class PresencaForm(ModelForm):

    class Meta:
        fields = '__all__'
        model = models.Presenca
