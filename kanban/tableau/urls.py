from django.urls import include, path
from rest_framework import routers
from . import views
from views import ColonneViewSet, TacheViewSet

router = routers.DefaultRouter()

router.register(r'colonnes', ColonneViewSet, basename='colonne')
router.register(r'taches', TacheViewSet, basename='tache')




urlpatterns = [
    path('', views.index, name='index'),
    path('api/', include(router.urls)),
]