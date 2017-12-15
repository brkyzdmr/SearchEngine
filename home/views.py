from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from urllib.request import urlopen
from django.template import loader
from home import forms
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)
def index(request):
    return render(request, 'html_files/Anasayfa.html', {})

def anahtarKelimeSaydirma(request):
    return render(request, 'html_files/AnahtarKelimeSaydirma.html', {})

def urlSiralama(request):
    return render(request, 'html_files/URLSiralama.html', {})

def anasayfa(request):
    return render(request, 'html_files/Anasayfa.html', {})

def search(request):
    form_eleman = forms
    if(request.method == 'GET'):
        form = forms.AnahtarKelimeSaydirma(request.POST)
        if(form.is_valid()):
            basarili = 'Tebrikler Başarılı!'
        #İstenmeyen durum.
        else:
            basarisiz = 'Hatalı!'
    return render(request, 'html_files/URLSiralamaSonuc.html', locals())
