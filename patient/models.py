from django.db import models

# Create your models here.
GENDER = [
    ('M', 'Masculin'),
    ('F', 'Feminin'),
]
GRPS = [
    ('O', 'O'),
    ('A', 'A'),
    ('B', 'B'),
    ('AB', 'AB'),
]
class Patient(models.Model):

    
    prenom = models.CharField(max_length=255)
    nom = models.CharField(max_length=100,)
    sexe = models.CharField(max_length=10, choices=GENDER, default='M')
    date_de_naissaince = models.DateField(blank=True, null=True)
    telephone = models.CharField(max_length=15, blank=True)
    groupe_sanguin = models.CharField(max_length=255, choices=GRPS, default='O')
    photo = models.CharField(max_length=255, blank=True)
    job = models.CharField(max_length=255, blank=True)
    emploi = models.CharField(max_length=255, blank=True)
    
    date_add = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.prenom + " " +self.nom