from django.urls import path
from api.views import criar

urlpatterns = [
    path('criar', criar, name='criar'),
]
