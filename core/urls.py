from django.contrib import admin
from django.urls import include, path

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="API - Challenge OLI Saúde",
      default_version='v1',
      description="O Desafio consistia em criar uma API capaz de gerenciar informações de saúde do cliente, fornecendo recursos para criar, editar, visualizar e listar clientes. Além disso, a API precisava calcular o risco de saúde com base nos problemas de saúde relatados pelos clientes, usando a fórmula score = (1 / (1 + e^(-2.8 + sd))) * 100. Esse calculo é baseado em um atributo cujo é o grau da gravidade do problema de saúde do cliente.",
      terms_of_service="https://www.suaapi.com/terms/",
      contact=openapi.Contact(name='Jeferson Dalarmi',email="dalarmi.jeferson@gmail.com",url='https://github.com/Jdalarmi',),
      
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
     path('swagger/', schema_view.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui'),
]