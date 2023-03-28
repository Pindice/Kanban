from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
# Create your views here.



def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def kanban(request):
    data = [
        {
            'id': 'board1',
            'title': 'À faire',
            'class': 'info',
            'item': [
                {
                    'title': 'Tâche 1',
                    'description': 'Description de la tâche 1'
                },
                {
                    'title': 'Tâche 2',
                    'description': 'Description de la tâche 2'
                }
            ]
        },
        {
            'id': 'board2',
            'title': 'En cours',
            'class': 'warning',
            'item': [
                {
                    'title': 'Tâche 3',
                    'description': 'Description de la tâche 3'
                }
            ]
        },
        {
            'id': 'board3',
            'title': 'Terminé',
            'class': 'success',
            'item': [
                {
                    'title': 'Tâche 4',
                    'description': 'Description de la tâche 4'
                }
            ]
        }
    ]
    return JsonResponse(data, safe=False)
