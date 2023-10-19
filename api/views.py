from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

from api.models import Client, ProblemsHealth
from .serializers import ClientSerializer, ClientSerializerOrder
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
        return JsonResponse({'error': 'Método não permitido'}, status=405)  # Método não permitido (405)

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


