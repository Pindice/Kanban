from django.shortcuts import render
from django.http import JsonResponse
from .models import Colonne, Tache
from rest_framework import viewsets
from .serializers import ColonneSerializer, TacheSerializer


def index(request):
    return render(request, 'tableau/index.html')

class ColonneViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Colonne.objects.all()
    serializer_class = ColonneSerializer

class TacheViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Tache.objects.all()
    serializer_class = TacheSerializer

    