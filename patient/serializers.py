from rest_framework import serializers
from .models import Patient

class PatientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Patient
        fields = ('prenom', 'nom', 'sexe', 'date_de_naissaince', 'telephone', 'groupe_sanguin', 'photo', 'job', 'emploi')
