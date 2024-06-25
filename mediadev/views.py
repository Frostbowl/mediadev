from django.shortcuts import render, redirect, get_object_or_404
from mediadev.models import Livre, Dvd, Cd, JeuDePlateau, Membre, Emprunt
from mediadev.forms import Ajoutlivre, Ajoutdvd, Ajoutcd, Ajoutplateau, Ajoutmembre, Ajoutemprunt

def homepage(request):
    return render(request, 'home/home.html')

def listeLivres(request):
    livres = Livre.objects.all()
    return render(request, 'livres/listeLivre.html', {'livres': livres})


def ajoutLivre(request):
    if request.method == 'POST':
        ajoutlivre = Ajoutlivre(request.POST)
        if ajoutlivre.is_valid():
            livre = Livre()
            livre.name = ajoutlivre.cleaned_data['name']
            livre.auteur = ajoutlivre.cleaned_data['auteur']
            livre.disponible = True
            livre.save()
            livres = Livre.objects.all()
            return render(request, 'livres/listeLivre.html', {'livres': livres})
    else:
        ajoutlivre = Ajoutlivre()
        return render(request, 'livres/ajoutlivre.html', {'ajoutlivre': ajoutlivre})


def listeDvds(request):
    dvds = Dvd.objects.all()
    return render(request, 'dvds/listeDvd.html', {'dvds': dvds} )

def ajoutDvd(request):
    if request.method == 'POST':
        ajoutdvd = Ajoutdvd(request.POST)
        if ajoutdvd.is_valid():
            dvd = Dvd()
            dvd.name = ajoutdvd.cleaned_data['name']
            dvd.realisateur = ajoutdvd.cleaned_data['realisateur']
            dvd.disponible = True
            dvd.save()
            dvds = Dvd.objects.all()
            return render(request, 'dvds/listeDvd.html', {'dvds': dvds})
    else:
        ajoutdvd = Ajoutdvd()
        return render(request, 'dvds/ajoutDvd.html', {'ajoutdvd': ajoutdvd})

def listeCds(request):
    cds = Cd.objects.all()
    return render(request, 'cds/listeCd.html', {'cds': cds})

def ajoutCd(request):
    if request.method == 'POST':
        ajoutcd = Ajoutcd(request.POST)
        if ajoutcd.is_valid():
            cd = Cd()
            cd.name = ajoutcd.cleaned_data['name']
            cd.artiste = ajoutcd.cleaned_data['artiste']
            cd.disponible = True
            cd.save()
            cds = Cd.objects.all()
            return render(request, 'cds/listeCd.html', {'cds':cds})
    else:
        ajoutcd = Ajoutcd()
        return render(request, 'cds/ajoutCd.html', {'ajoutcd': ajoutcd})

def listePlateaux(request):
    plateaux = JeuDePlateau.objects.all()
    return render(request, 'plateaux/listePlateau.html', {'plateaux': plateaux})

def ajoutPlateau(request):
    if request.method == 'POST':
        ajoutplateau = Ajoutplateau(request.POST)
        if ajoutplateau.is_valid():
            plateau = JeuDePlateau()
            plateau.name = ajoutplateau.cleaned_data['name']
            plateau.createur = ajoutplateau.cleaned_data['createur']
            plateau.disponible = True
            plateau.save()
            plateaux = JeuDePlateau.objects.all()
            return render(request, 'plateaux/listePlateau.html', {'plateaux': plateaux})
    else:
        ajoutplateau = Ajoutplateau()
        return render(request, 'plateaux/ajoutPlateau.html', {'ajoutplateau': ajoutplateau})

def listeMembre(request):
    membres = Membre.objects.all()
    return render(request, 'membres/listeMembre.html', {'membres': membres})

def ajoutMembre(request):
    if request.method == 'POST':
        ajoutmembre = Ajoutmembre(request.POST)
        if ajoutmembre.is_valid():
            membre = Membre()
            membre.lastname = ajoutmembre.cleaned_data['lastname']
            membre.firstname = ajoutmembre.cleaned_data['firstname']
            membre.bloque = False
            membre.save()
            membres = Membre.objects.all()
            return render(request, 'membres/listeMembre.html', {'membres': membres})
    else:
        ajoutmembre = Ajoutmembre()
        return render(request, 'membres/ajoutMembre.html', {'ajoutmembre': ajoutmembre})

def creer_emprunt(request):
    if request.method == 'POST':
        form = Ajoutemprunt(request.POST)
        if form.is_valid():
            membre = form.cleaned_data['membre']
            media_type = form.cleaned_data['media_type']
            media_id = form.cleaned_data['media_id']
            media_name = form.cleaned_data['media_name']

            if Emprunt.objects.filter(membre=membre).count() >= 3:
                return render(request, 'emprunts/ajoutEmprunt.html', {'form': form, 'error': 'Ce membre à déjà trois emprunts.'})
            
            if Emprunt.objects.filter(media_type=media_type, media_id=media_id).exists():
                return render(request, 'emprunts/ajoutEmprunt.html', {'form': form, 'error': 'Ce média est déjà emprunté'})
            
            if media_type == 'livre':
                media = Livre.objects.get(id=media_id)
                media_name = media.name
            elif media_type == 'dvd':
                media = Dvd.objects.get(id=media_id)
                media_name = media.name
            elif media_type == 'cd':
                media = Cd.objects.get(id=media_id)
                media_name=media.name
            else:
                media_name='Inconnu'    

            Emprunt.objects.create(
                membre = membre,
                media_type = media_type,
                media_id = media_id,
                media_name=media_name
            )
            return redirect('listeemprunt')
    else:
        form = Ajoutemprunt()

    return render(request, 'emprunts/ajoutEmprunt.html', {'form': form})

def listeEmprunt(request):
    emprunts = Emprunt.objects.all()
    return render(request, 'emprunts/listeEmprunt.html', {'emprunts': emprunts})
