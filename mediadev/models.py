from django.db import models

class Livre(models.Model):
    name = models.fields.CharField(max_length=150)
    auteur = models.fields.CharField(max_length=150)
    disponible = models.BooleanField(default=True)

class Dvd(models.Model):
    name = models.CharField(max_length=150)
    realisateur = models.CharField(max_length=150)
    disponible = models.BooleanField(default=True)

class Cd(models.Model):
    name = models.CharField(max_length=150)
    artiste = models.CharField(max_length=150)
    disponible = models.BooleanField(default=True)

class JeuDePlateau(models.Model):
    name = models.CharField(max_length=150)
    createur = models.CharField(max_length=150, default='Unknown')
    disponible = models.BooleanField(default=True)

class Membre(models.Model):
    lastname = models.CharField(max_length=150)
    firstname = models.CharField(max_length=150)
    bloque = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.firstname} {self.lastname}'
    
    def active_loans(self):
        return self.emprunt_set.filter(date_retour_isnull=True).count()

class Emprunt(models.Model):
    media_choix = [
        ('livre', 'Livre'),
        ('dvd', 'Dvd'),
        ('cd', 'Cd'),
    ]

    membre = models.ForeignKey(Membre, on_delete=models.CASCADE)
    media_type = models.CharField(max_length=150, choices=media_choix)
    media_id = models.PositiveIntegerField()
    media_name = models.CharField(max_length=150, default='Unknow')

    def __str__(self):
        return f"{self.membre} borrowed {self.media_type} {self.media_id} {self.media_name}"