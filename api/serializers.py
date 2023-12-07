from rest_framework import serializers
from api.models import Game

class GameSerializer(serializers.ModelSerializer):
    # reviews = serializers.StringRelatedField(many=True)
   
    class Meta:
        #Indico con que modelo se va a corresponder el serializador
        model = Game
        #listado defino los campos de la clase Game que quiero serializar
        fields = ['id', 'title', 'release_date', 'developer', 'banner']

# class ReviewSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Review
#         fields = ['']