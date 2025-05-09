from django.urls import path
from .views import registro_usuario
from .views import login
from . import views

urlpatterns = [
    path('', views.home, name='index'),
    path('registro/', views.registro_usuario, name='registro'),
    path('login/', views.login, name= 'login')
]