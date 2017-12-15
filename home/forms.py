from django import forms

class URLSiralamaForm(forms.Form):
    words = forms.CharField(label='Your name', max_length=100)
