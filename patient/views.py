from django.shortcuts import render
# from rest_framework import viewsets
from rest_framework.views import APIView
from .models import Patient
from .serializers import PatientSerializer
from rest_framework.response import Response
# from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http import HttpResponse, JsonResponse
from rest_framework import status


class PatientAPIView(APIView):

    
    serializer_class = PatientSerializer

    def get(self, request, pk=None):

        if pk:    
            queryset = Patient.objects.filter(pk=pk)
            serializer = PatientSerializer(queryset, many=True)
            return JsonResponse(serializer.data, safe=False)
            
        else:
            queryset = Patient.objects.all()
            serializer = PatientSerializer(queryset, many=True)
            return JsonResponse(serializer.data, safe=False)
    
    def post(self, request):
        data = JSONParser().parse(request)
        serializer = PatientSerializer(data=data)
        
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)

        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def put(self, request, pk):
        patient = Patient.objects.get(pk=pk)
        data = JSONParser().parse(request)

        values_list = ['prenom', 'nom', 'sexe', 'date_de_naissaince', 'telephone', 'groupe_sanguin', 'photo', 'job', 'emploi']

        for key in values_list:
            if key in data:
                patient.__setattr__(key, data[key])
                patient.save()
                
        serializer = PatientSerializer(patient)
        return JsonResponse(serializer.data, status=status.HTTP_200_OK)
        # return JsonResponse({'Mise à jour':"Succès"}, status=status.HTTP_200_OK)



    def delete(self, request, pk):
        queryset = Patient.objects.get(pk=pk)

        queryset.delete()

        return JsonResponse({'Supression':"True"}, status=status.HTTP_200_OK)

    
