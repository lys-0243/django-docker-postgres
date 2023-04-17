from django.db import models

# Create your models here.
GENDER = [
    ('M', 'Masculin'),
    ('F', 'Feminin'),
]

class Medecin(models.Model):

    
    prenom = models.CharField(max_length=255)
    nom = models.CharField(max_length=100,)
    sexe = models.CharField(max_length=10, choices=GENDER, default='M')
    telephone = models.CharField(max_length=15)
    photo = models.CharField(max_length=255, blank=True)
    specialisation = models.CharField(max_length=255)
    
    date_add = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.prenom + " " +self.nom