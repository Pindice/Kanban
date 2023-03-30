from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('colonnes/', views.get_colonnes, name='get_colonnes'),
    path('colonnes/create/', views.create_colonne, name='create_colonne'),
    path('colonnes/delete/<int:colonne_id>/', views.delete_colonne, name='delete_colonne'),
    path('colonnes/update/<int:colonne_id>/', views.update_colonne, name='update_colonne'),
    path('taches/create/', views.create_tache, name='create_tache'),
    path('taches/delete/<int:tache_id>/', views.delete_tache, name='delete_tache'),
    path('taches/update/<int:tache_id>/', views.update_tache, name='update_tache'),
    path('update_data/', views.update_data, name='update_data')
]