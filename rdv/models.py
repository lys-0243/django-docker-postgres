from django.db import models
from patient.models import Patient
from medecin.models import Medecin

# Create your models here.
class Rendezvous(models.Model):

    date_add = models.DateTimeField(auto_now_add=True)
    
    patient = models.ForeignKey(Patient, related_name="patrient_reserved", on_delete=models.CASCADE,)
    medecin = models.ForeignKey(Medecin, related_name="medecin_reserved", on_delete=models.CASCADE,)
    date_de_rdv = models.DateField()
    
    motif    = models.TextField(max_length=255)

    def __str__(self):
        return self.patient+ ' Pour ' +self.medecin