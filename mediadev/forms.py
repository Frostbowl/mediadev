from django import forms
from .models import Membre, Emprunt

class Ajoutlivre(forms.Form):
    name = forms.CharField(required=True, max_length=150)
    auteur = forms.CharField(required=True, max_length=150)

class Ajoutdvd(forms.Form):
    name = forms.CharField(required=True, max_length=150)
    realisateur = forms.CharField(required=True, max_length=150)

class Ajoutcd(forms.Form):
    name = forms.CharField(required=True, max_length=150)
    artiste = forms.CharField(required=True, max_length=150)

class Ajoutplateau(forms.Form):
    name = forms.CharField(required=True, max_length=150)
    createur = forms.CharField(required=True, max_length=150)

class Ajoutmembre(forms.Form):
    lastname = forms.CharField(required=True, max_length=150)
    firstname = forms.CharField(required=True, max_length=150)

class Ajoutemprunt(forms.ModelForm):
    class Meta:
        model = Emprunt
        fields = ['membre', 'media_type', 'media_id', 'media_name']