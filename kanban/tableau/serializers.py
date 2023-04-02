from rest_framework import serializers
from tableau.models import Colonne, Tache

class ColonneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Colonne
        fields = '__all__'


class TacheSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tache
        fields = '__all__'
