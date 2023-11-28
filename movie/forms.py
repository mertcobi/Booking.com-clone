from django import forms
from .models import *

class FormOlustur(forms.ModelForm):
    class Meta:
        model = Otel
        fields = ['title','adres','image','rating','map','review_count','price','tax','cancel','room','is_active']
        labels ={
            'title':'Otel Adi',
            'image':'Otel Resmi',
            'adres':'adres',
            'rating':'otel derecesi',
            'map':'haritada göster',
            'review_count':'değerelendirme',
            'price':'fiyat',
            'tax':'vergi fiyatı',
            'cancel':'ücretsiz iptal',
            'room':'oda yatak sayisi',
        },

        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control w-50 mb-2','placeholder':'Otel adi gir'}),
            'image':forms.FileInput(attrs={'class':'form-control w-50'}),
            'adres':forms.TextInput(attrs={'class':'form-control w-50','placeholder':'fiyat giriniz:'}),
            'rating':forms.NumberInput(attrs={'class':'form-control w-50','placeholder':'fiyat giriniz:'}),
            'map':forms.TextInput(attrs={'class':'form-control w-50','placeholder':'fiyat giriniz:'}),
            'review_count':forms.TextInput(attrs={'class':'form-control w-50','placeholder':'fiyat giriniz:'}),
            'price':forms.TextInput(attrs={'class':'form-control w-50','placeholder':'fiyat giriniz:'}),
            'tax':forms.TextInput(attrs={'class':'form-control w-50','placeholder':'fiyat giriniz:'}),
            'cancel':forms.TextInput(attrs={'class':'form-control w-50','placeholder':'fiyat giriniz:'}),
            'room':forms.Textarea(attrs={'class':'form-control w-50'}),
            'is_active':forms.CheckboxInput(attrs={'class':'form-check-input d-block w-5'}),
        }