from rest_framework import serializers
from .models import Medecin

class MedecinSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Medecin
        fields = ('prenom', 'nom', 'sexe', 'telephone', 'photo', 'specialisation')
