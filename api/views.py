from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from api.models import Client, ProblemsHealth
from .serializers import ClientSerializer, ClientSerializerOrder, ClientSerializerUpdate
from drf_yasg.utils import swagger_auto_schema
from rest_framework.exceptions import APIException
import logging
from django.http import JsonResponse

logger = logging.getLogger(__name__)

@swagger_auto_schema(method='post', request_body=ClientSerializer)
@api_view(['POST'])
def criar(request):
    """
    Endpoint para criar um novo cliente.
    """
    if request.method != 'POST':
        logger.error('Método não permitido. Apenas requisições POST são aceitas.')
        return JsonResponse({'error': 'Método não permitido'}, status=405) 

    logger.debug('Requisição POST recebida com dados: %s', request.data)
    
    serializer = ClientSerializer(data=request.data)
    
    if serializer.is_valid():
        logger.debug('Dados válidos. Salvando o objeto Client no banco de dados.')
        serializer.save()
        return JsonResponse(serializer.data, status=201) 
    else:
        logger.error('Dados inválidos: %s', serializer.errors)
        return JsonResponse(serializer.errors, status=400)  


@api_view(['GET'])
def order(request):
    client = Client.objects.all()
    serializer = ClientSerializerOrder(client, many=True)
    return Response(serializer.data)

@swagger_auto_schema(method='put', request_body=ClientSerializerUpdate)
@api_view(['PUT'])
def client_edit(request, pk):
    client = Client.objects.get(id=pk)
    
    serializer = ClientSerializerUpdate(client, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)