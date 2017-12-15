from django.forms import *
class AnahtarKelimeSaydirma(Form):
    word = CharField(max_length=50,required=True)
    url = CharField(max_length=50,required=True)
