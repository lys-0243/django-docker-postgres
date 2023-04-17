from django.shortcuts import render
# from rest_framework import viewsets
from rest_framework.views import APIView
from .models import Medecin
from .serializers import MedecinSerializer
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.http import HttpResponse, JsonResponse
from rest_framework import status
from django.db.models import Q


class MedecinAPIView(APIView):

    
    serializer_class = MedecinSerializer

    def get(self, request, pk=None):

        if pk:    
            queryset = Medecin.objects.filter(pk=pk)
            serializer = MedecinSerializer(queryset, many=True)
            return JsonResponse(serializer.data, safe=False)
            
        else:
            queryset = Medecin.objects.all()
            serializer = MedecinSerializer(queryset, many=True)
            return JsonResponse(serializer.data, safe=False)
    
    def post(self, request):
        
        data = JSONParser().parse(request)
        serializer = MedecinSerializer(data=data)
        
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)

        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        medecin = Medecin.objects.get(pk=pk)
        data = JSONParser().parse(request)

        values_list = ['prenom', 'nom', 'sexe', 'telephone', 'specialisation']

        for key in values_list:
            if key in data:
                medecin.__setattr__(key, data[key])
                medecin.save()
                
        serializer = Medecin(medecin)
        
        return JsonResponse({"Mise à jour":"Succès"}, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        queryset = Medecin.objects.get(pk=pk)

        queryset.delete()

        return JsonResponse({'Supression':"True"}, status=status.HTTP_200_OK)

    
def search(self, slug):
    slug = slug.lower()

    queryset = Medecin.objects.filter(Q(prenom__iexact = slug) | Q(nom__iexact=slug) | Q(specialisation__iexact=slug))

    serializer = MedecinSerializer(queryset, many=True)

    return JsonResponse(serializer.data, safe=False)

