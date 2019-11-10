from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _

from datetime import date

# Create your models here.

class Presenca(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(null=False, blank=False, max_length=100)
    date = models.DateField(null=False, blank=False, auto_now=False, auto_now_add=False)

    def save(self, *args, **kwargs):
        hoje = date.today()
        if self.pk is None and self.date != hoje:
            raise ValidationError(_('Data da presença tem de ser hoje.'))
        super(Presenca, self).save(*args, **kwargs)
