from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^AnahtarKelimeSaydirma/$', views.anahtarKelimeSaydirma, name='anahtarKelimeSaydirma'),
    url(r'^URLSiralama/$', views.urlSiralama, name='urlSiralama'),
 ]
