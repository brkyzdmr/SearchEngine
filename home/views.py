from django.shortcuts import render
from django.http import HttpResponseRedirect
from home.forms import URLSiralamaForm


def index(request):
    return render(request, 'html_files/Anasayfa.html', {})

def anahtarKelimeSaydirma(request):
    return render(request, 'html_files/AnahtarKelimeSaydirma.html', {})

def urlSiralama(request):
    return render(request, 'html_files/URLSiralama.html', {})

def anasayfa(request):
    return render(request, 'html_files/Anasayfa.html', {})
