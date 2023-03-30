from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Colonne, Tache


def index(request):
    return render(request, 'tableau/index.html')

def get_colonnes(request):
    colonnes = Colonne.objects.all().values()
    colonnes_list = list(colonnes)
    for colonne in colonnes_list:
        taches = Tache.objects.filter(colonne_id=colonne['id']).values()
        colonne['item'] = list(taches)
    return JsonResponse(colonnes_list, safe=False)

def create_colonne(request):
    pos_col = request.POST['pos_col']
    nom_col = request.POST['nom_col']
    colonne = Colonne(pos_col=pos_col, nom_col=nom_col)
    colonne.save()
    return JsonResponse({'message': 'Colonne créée avec succès!'})

def delete_colonne(request, colonne_id):
    colonne = Colonne.objects.get(id=colonne_id)
    colonne.delete()
    return JsonResponse({'message': 'Colonne supprimée avec succès!'})

def update_colonne(request, colonne_id):
    colonne = Colonne.objects.get(id=colonne_id)
    colonne.pos_col = request.POST['pos_col']
    colonne.nom_col = request.POST['nom_col']
    colonne.save()
    return JsonResponse({'message': 'Colonne mise à jour avec succès!'})

def create_tache(request):
    pos_task = request.POST['pos_task']
    nom_task = request.POST['nom_task']
    colonne_id = request.POST['colonne_id']
    tache = Tache(pos_task=pos_task, nom_task=nom_task, colonne_id=colonne_id)
    tache.save()
    return JsonResponse({'message': 'Tâche créée avec succès!'})

def delete_tache(request, tache_id):
    tache = Tache.objects.get(id=tache_id)
    tache.delete()
    return JsonResponse({'message': 'Tâche supprimée avec succès!'})

def update_tache(request, tache_id):
    tache = Tache.objects.get(id=tache_id)
    tache.pos_task = request.POST['pos_task']
    tache.nom_task = request.POST['nom_task']
    tache.colonne_id = request.POST['colonne_id']
    tache.save()
    return JsonResponse({'message': 'Tâche mise à jour avec succès!'})
