from django.db import models
from contatos.models import Contact
from django import forms

# Create your models here.

class FormContato(forms.ModelForm):
    class Meta:
        model = Contact
        exclude = ('mostrar',)