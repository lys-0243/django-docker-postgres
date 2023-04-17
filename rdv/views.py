from django.shortcuts import render
from rest_framework.views import APIView
from .models import Rendezvous
from .serializers import RendezvousSerializer
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.http import HttpResponse, JsonResponse
from rest_framework import status

from medecin.models import Medecin
from patient.models import Patient

class RdvAPIView(APIView):
    
    serializer_class = RendezvousSerializer

    def get(self, request, pk=None):

        if pk:    
            queryset = Rendezvous.objects.filter(pk=pk)
            serializer = RendezvousSerializer(queryset, many=True)
            return JsonResponse(serializer.data, safe=False)
            
        else:
            queryset = Rendezvous.objects.all()
            serializer = RendezvousSerializer(queryset, many=True)
            return JsonResponse(serializer.data, safe=False)
    
    def post(self, request):
        data = JSONParser().parse(request)
        medecinID = data['medecin']
        patientID = data['patient']

        medecinObj = Medecin.objects.get(pk=medecinID)
        patientObj = Patient.objects.get(pk=patientID)

        newData = {
            "patient":patientObj,
            "medecin":medecinObj,
            "date_de_rdv":data['date_de_rdv'],
            "motif":data['motif'],
        }

        store_rdv = Rendezvous.objects.create(**newData)
        store_rdv.save()
        
        # serializer = RendezvousSerializer(data=store_rdv)
        
        # if serializer.is_valid():
            
        return JsonResponse({"Succes":"RDV Saved"}, status=status.HTTP_201_CREATED)

        # return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        patient = Rendezvous.objects.get(pk=pk)
        data = JSONParser().parse(request)

        values_list = ['nom', 'adresse']

        for key in values_list:
            if key in data:
                patient.__setattr__(key, data[key])
                patient.save()
                
        serializer = RendezvousSerializer(patient)
        return JsonResponse(serializer.data, status=status.HTTP_200_OK)
        # return JsonResponse({'Mise à jour':"Succès"}, status=status.HTTP_200_OK)


    def delete(self, request, pk):
        queryset = Rendezvous.objects.get(pk=pk)

        queryset.delete()

        return JsonResponse({'Succes':"Delete"}, status=status.HTTP_200_OK)

    

