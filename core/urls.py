from django.urls import path
from . import views
from .views import inicio

urlpatterns = [
    # Página de inicio
     path('', inicio, name='inicio'),

    # Registro de usuarios
    path('registro/', views.registro_usuario, name='registro'),

    # Login de usuarios
    path('login/', views.login_usuario, name='login'),

    # Paneles de usuario (Coordinador, Docente, Estudiante, Acudiente)
    path('panel-docente/', views.panel_docente, name='panel_docente'),
    path('panel-estudiante/', views.panel_estudiante, name='panel_estudiante'),
    path('panel-coordinador/', views.panel_coordinador, name='panel_coordinador'),
    path('panel-acudiente/', views.panel_acudiente, name='panel_acudiente'),

    # Rutas para la gestión del currículo y áreas educativas por el Coordinador Académico
    # Niveles Educativos
    path('coordinador/niveles/', views.lista_niveles, name='lista_niveles'),
    path('coordinador/niveles/nuevo/', views.crear_nivel, name='crear_nivel'),
    path('coordinador/niveles/editar/<int:pk>/', views.editar_nivel, name='editar_nivel'),
    path('coordinador/niveles/eliminar/<int:pk>/', views.eliminar_nivel, name='eliminar_nivel'),

    # Grados
    path('coordinador/grados/', views.lista_grados, name='lista_grados'),
    path('coordinador/grados/nuevo/', views.crear_grado, name='crear_grado'),
    path('coordinador/grados/editar/<int:pk>/', views.editar_grado, name='editar_grado'),
    path('coordinador/grados/eliminar/<int:pk>/', views.eliminar_grado, name='eliminar_grado'),

    # Áreas
    path('coordinador/areas/', views.lista_areas, name='lista_areas'),
    path('coordinador/areas/nuevo/', views.crear_area, name='crear_area'),
    path('coordinador/areas/editar/<int:pk>/', views.editar_area, name='editar_area'),
    path('coordinador/areas/eliminar/<int:pk>/', views.eliminar_area, name='eliminar_area'),

    # Asignaturas
    path('coordinador/asignaturas/', views.lista_asignaturas, name='lista_asignaturas'),
    path('coordinador/asignaturas/nuevo/', views.crear_asignatura, name='crear_asignatura'),
    path('coordinador/asignaturas/editar/<int:pk>/', views.editar_asignatura, name='editar_asignatura'),
    path('coordinador/asignaturas/eliminar/<int:pk>/', views.eliminar_asignatura, name='eliminar_asignatura'),

    # Temas
    path('coordinador/temas/', views.lista_temas, name='lista_temas'),
    path('coordinador/temas/nuevo/', views.crear_tema, name='crear_tema'),
    path('coordinador/temas/editar/<int:pk>/', views.editar_tema, name='editar_tema'),
    path('coordinador/temas/eliminar/<int:pk>/', views.eliminar_tema, name='eliminar_tema'),

    # Logros
    path('coordinador/logros/', views.lista_logros, name='lista_logros'),
    path('coordinador/logros/nuevo/', views.crear_logro, name='crear_logro'),
    path('coordinador/logros/editar/<int:pk>/', views.editar_logro, name='editar_logro'),
    path('coordinador/logros/eliminar/<int:pk>/', views.eliminar_logro, name='eliminar_logro'),
]
