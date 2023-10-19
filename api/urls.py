from django.urls import path
from api.views import criar, order

urlpatterns = [
    path('create/', criar, name='create'),
    path('order/', order, name='order'),
]
