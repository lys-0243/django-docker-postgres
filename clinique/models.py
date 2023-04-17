from django.db import models


class Clinique(models.Model):

    nom = models.CharField(max_length=100,)
    adresse = models.TextField(max_length=255)

    date_add = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nom