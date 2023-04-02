from django.shortcuts import render
from django.http import JsonResponse
from .models import Colonne, Tache
from rest_framework import viewsets
from .serializers import ColonneSerializer, TacheSerializer


def index(request):
    colonnes = Colonne.objects.all()
    context = {'colonnes': colonnes}
    return render(request, 'tableau/index.html', context)

class ColonneViewSet(viewsets.ModelViewSet):
    queryset = Colonne.objects.all()
    serializer_class = ColonneSerializer

class TacheViewSet(viewsets.ModelViewSet):
    queryset = Tache.objects.all()
    serializer_class = TacheSerializer

    