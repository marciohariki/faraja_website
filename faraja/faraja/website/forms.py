from faraja.website.models import *
from tinymce.widgets import TinyMCE
from django.forms import ModelForm
from django import forms
class WhoWeAreForm(ModelForm):
    texto = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))
    
    