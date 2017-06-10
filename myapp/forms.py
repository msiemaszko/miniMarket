from django import forms
from .models import Produkty

class PostForm(forms.ModelForm):
    imie_nazwisko = forms.CharField(max_length=120, widget=forms.TextInput({
        'class': 'form-control',
        'style': 'width: 50%',
    }))
    ulica = forms.CharField(max_length=50, widget=forms.TextInput({
        'class': 'form-control',
        'style': 'width: 50%',
    }))
    miasto = forms.CharField(max_length=50, widget=forms.TextInput({
        'class': 'form-control',
        'style': 'width: 50%',
    }))
    telefon = forms.CharField(max_length=50, widget=forms.TextInput({
        'class': 'form-control',
        'style': 'width: 50%',
        'match': '[0-9]',
    }))

    class Meta:
        model = Produkty
        fields = ('imie_nazwisko', 'ulica', 'miasto', 'telefon',)
