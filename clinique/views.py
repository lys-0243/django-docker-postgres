from django.shortcuts import render
from rest_framework.views import APIView
from .models import Clinique
from .serializers import CliniqueSerializer
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.http import HttpResponse, JsonResponse
from rest_framework import status


class CliniqueAPIView(APIView):
    
    serializer_class = CliniqueSerializer

    def get(self, request, pk=None):

        if pk:    
            queryset = Clinique.objects.filter(pk=pk)
            serializer = CliniqueSerializer(queryset, many=True)
            return JsonResponse(serializer.data, safe=False)
            
        else:
            queryset = Clinique.objects.all()
            serializer = CliniqueSerializer(queryset, many=True)
            return JsonResponse(serializer.data, safe=False)
    
    def post(self, request):
        data = JSONParser().parse(request)
        serializer = CliniqueSerializer(data=data)
        
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)

        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        patient = Clinique.objects.get(pk=pk)
        data = JSONParser().parse(request)

        values_list = ['nom', 'adresse']

        for key in values_list:
            if key in data:
                patient.__setattr__(key, data[key])
                patient.save()
                
        serializer = CliniqueSerializer(patient)
        return JsonResponse(serializer.data, status=status.HTTP_200_OK)
        # return JsonResponse({'Mise à jour':"Succès"}, status=status.HTTP_200_OK)


    def delete(self, request, pk):
        queryset = Clinique.objects.get(pk=pk)

        queryset.delete()

        return JsonResponse({'Succes':"Delete"}, status=status.HTTP_200_OK)

    

