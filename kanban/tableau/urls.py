from django.urls import path
from . import views
from .views import kanban


urlpatterns = [
    path('', views.index, name='index'),
    path('kanban/', kanban, name='kanban')
]