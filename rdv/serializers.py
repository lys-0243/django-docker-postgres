from rest_framework import serializers
from .models import Rendezvous

class RendezvousSerializer(serializers.HyperlinkedModelSerializer):
    patient = serializers.HyperlinkedRelatedField(
        many=False,
        read_only=True,
        view_name='patient_name'
    )
    medecin = serializers.HyperlinkedRelatedField(
        many=False,
        read_only=True,
        view_name='patient_name'
    )
    class Meta:
        model = Rendezvous
        fields = ('patient', 'medecin', 'date_de_rdv', 'motif')
