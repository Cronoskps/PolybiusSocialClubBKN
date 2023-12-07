from django.shortcuts import render
from django.http import HttpResponse

#importo el modelo de Game
from api.models import Game

#se importa el serializador creado
from api import serializers

#Se importan funcionalides del la libreria rest_framework
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
def index(request):
    return HttpResponse('<h1>Hola mundo Django</h1>')


@api_view(['GET']) #solo pueda ser accecido si la petición es GET
def get_games(request):
    """
    Lista todos los juegos
    """
    #se buscan todos los registros guardados en la base del modelo Game
    games = Game.objects.all()
    #cuando estás serializando múltiples instancias de un modelo
    serializer = serializers.GameSerializer(games, many=True)
    #Response es una clase que me permite devolver una respuesta
    #que cumple con los estandares de API-REST
    return Response(serializer.data)

@api_view(['POST']) #solo pueda ser accecido si la petición es POST
def create_game(request):
    """
    Crear un Juego
    """
    #Se serializa los datos recibidos desde el formulario
    serializer = serializers.GameSerializer(data=request.data)
    #Se ejecutan las validaciones
    if serializer.is_valid():
        #Se registra en base de datos
        serializer.save()
        #Se genera la respuesta que deseamos devolver
        response = {'status':'Ok',
                    'message':'Juego creado exitosamente',
                    'data':serializer.data}
        return Response(data= response, status=status.HTTP_201_CREATED)
    response = {'status':'Error',
                'message':'No se pudo crear el Juego',
                'errors':serializer.errors}
    return Response(data=response, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def detail_game(request, id):
    """
    Muestra una pelicula segun id.
    """
    try:
        #Se busca el juego en base por el id
        game = Game.objects.get(pk=id)        
    except Game.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,data='Recurso no encontrado')

    serializer = serializers.GameSerializer(game)
    return Response(serializer.data)

@api_view(['DELETE'])
def delete_game(request, id):
    """
    Eliminar un juego segun id.
    """
    try:
        #Se busca el juego en base por el id
        game = Game.objects.get(pk=id)        
    except Game.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,data='Recurso no encontrado')
    #elimina el registro de la base de datos
    game.delete()
    return Response({'message':'Se eliminó el Juego'},status=status.HTTP_200_OK)


@api_view(['PUT'])
def update_game(request, id):
    """
    Actualiza un Juego.
    """
    try:
        game = Game.objects.get(pk=id)
    except Game.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,data='Recurso no encontrado')
    
    #Se realiza proceso de serializacion, con el juego encontrado
    # y los datos que fueron enviados desde el cliente
    serializer = serializers.GameSerializer(game, data=request.data)
    if serializer.is_valid():
        serializer.save()
        response = {'status':'Ok',
                    'message':'Juego modificado exitosamente',
                    'data':serializer.data}
        return Response(data=response)
    response = {'status':'Error',
                'message':'No se pudo modificar el juego',
                'errors':serializer.errors}
    return Response(data=response, status=status.HTTP_400_BAD_REQUEST)
