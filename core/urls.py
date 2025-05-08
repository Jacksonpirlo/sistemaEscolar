from django.urls import path
from .views import registro_usuario
from . import views

urlpatterns = [
    path('', views.home, name='index'),
    path('registro/', registro_usuario, name='registro')
]