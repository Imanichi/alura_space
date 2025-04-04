from django.urls import path
from galeria.views import index
from galeria.views import imagem

urlpatterns = [
    path('', index),
]