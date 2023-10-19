from django.urls import path
from api.views import criar, order, client_edit

urlpatterns = [
    path('create/', criar, name='create'),
    path('order/', order, name='order'),
    path('edit/<str:pk>', client_edit, name='edit'),
]
