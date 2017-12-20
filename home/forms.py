from django.forms import *
from django import forms

class AnahtarKelimeSaydirmaForm(forms.Form):
    word = forms.CharField(label='Anahtar Kelime ', max_length=100)
    url = forms.CharField(label='Aranacak Url ', max_length=100)

class URLSiralamaForm(forms.Form):
    words = forms.CharField(label='Anahtar Kelimeler ', max_length=100)
    urls = forms.CharField(label='Aranacak Url ', widget=forms.widgets.Textarea())
