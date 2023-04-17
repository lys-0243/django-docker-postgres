from rest_framework import serializers
from .models import Clinique

class CliniqueSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Clinique
        fields = ('nom', 'adresse')
