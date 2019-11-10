from django.core.exceptions import ValidationError
from django.test import TestCase

from minhaapp.models import Presenca

from datetime import datetime, timedelta, date

# Create your tests here.
class PresencaTestCase(TestCase):

    def test_presenca_antes_de_hoje(self):
        with self.assertRaises(ValidationError):
            aluno = Presenca.objects.create(name="aluno2", date=date.today()-timedelta(days=1))

    def test_presenca_hoje(self):
        aluno = Presenca.objects.create(name="aluno1", date=date.today())
        self.assertEquals(aluno.date, date.today())

    def test_presenca_depois_hoje(self):
        with self.assertRaises(ValidationError):
            aluno = Presenca.objects.create(name="aluno2", date=date.today()+timedelta(days=1))

