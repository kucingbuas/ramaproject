from django import forms
from django.db.models import fields
from django.forms import widgets
from .models import Artikel

class ArtikelForms(forms.ModelForm):
    class Meta:
        model = Artikel
        fields = ('nama', 'judul', 'body',)
        widgets = {
            "nama" : forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'type':'text',
                    'required':True
                }),
                # cols="30" rows="10" class="form-control"
            "judul" : forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'type':'text',
                    'required':True
                }),
                # cols="30" rows="10" class="form-control"
            "body" : forms.Textarea(
                attrs={
                    'class': 'form-control textarea',
                    'rows': 10,
                    'cols':80,
                    'required':True
                }),
        }