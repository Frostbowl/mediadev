from django.contrib import admin
from django.urls import path
from mediadev import views

urlpatterns = [
    path('', views.homepage, name='home'),
    path('livre/',views.listeLivres, name="listelivres"),
    path('ajoutlivre/', views.ajoutLivre, name="ajoutLivre"),
    path('dvd/', views.listeDvds, name='listedvds'),
    path('ajoutdvd/', views.ajoutDvd, name='ajoutDvd'),
    path('cd/', views.listeCds, name='listecds'),
    path('ajoutcd/', views.ajoutCd, name='ajoutcd'),
    path('plateau/', views.listePlateaux, name='listeplateaux'),
    path('ajoutplateau/', views.ajoutPlateau, name="ajoutplateau"),
    path('membre/', views.listeMembre, name="listemembre"),
    path('ajoutmembre/', views.ajoutMembre, name="ajoutmembre"),
    path('emprunt/', views.listeEmprunt, name="listeemprunt"),
    path('ajoutemprunt/', views.creer_emprunt, name="ajoutemprunt"),
]
