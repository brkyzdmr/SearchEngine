from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponse, Http404
from urllib.request import urlopen
from django.template import loader
from urllib.request import urlopen
from django.views.decorators.csrf import csrf_exempt
from .forms import *
import re
from bs4 import BeautifulSoup

def index(request):
    return render(request, 'html_files/Anasayfa.html', {})

def anahtarKelimeSaydirma(request):
    if request.method == "POST":
        word = request.POST['word']
        url = request.POST['url']

        number = getUrlData(word.lower(), url)
        form = AnahtarKelimeSaydirmaForm()
        context = {
            "word": word,
            "url": url,
            "number": number
        }
        return render(request, 'html_files/Sonuc1.html', context)
    else:
        form = AnahtarKelimeSaydirmaForm()
        context = {
            "form": form
        }
        return render(request, 'html_files/AnahtarKelimeSaydirma.html', context)

def getUrlData(word, url):
    response = urlopen(url)
    data = str(response.read(), encoding='utf-8')
    cleanData = cleanHtml(data)
    number = findWordInData(word, cleanData)

    return number

def cleanHtml(raw_html):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', raw_html)
    cleantext = cleantext.replace('\\n', ' ').replace('\\r', '')
    return cleantext

def findWordInData(word, data):
    num = data.lower().split().count(word)
    return num

def urlSiralama(request):
    if request.method == "POST":
        words = request.POST['words']
        urls = request.POST['urls']

        wordList = words.replace(" ", "").split(',')
        urlList = urls.replace(" ", "").split(',')

        print(wordList)
        dataList = []
        for word in wordList:
            for url in urlList:
                dataList.append(getUrlData(word, url))

        print(dataList)
        context = {
            "word": words,
            "url": urls,
        }
        return render(request, 'html_files/Sonuc2.html', context)
    else:
        form = URLSiralamaForm()
        context = {
            "form": form
        }
        return render(request, 'html_files/URLSiralama.html', context)
