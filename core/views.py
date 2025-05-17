from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth import login
from .forms import LoginForm, RegistroUsuarioForm, NivelEducativoForm, GradoForm, AreaForm, AsignaturaForm, TemaForm, LogroForm
from .models import Usuario, NivelEducativo, Grado, Area, Asignatura, Tema, Logro
from django.contrib.auth.decorators import login_required, user_passes_test

# Función de acceso para Coordinador
def es_coordinador(user):
    return user.rol.nombre == 'Coordinador Académico'

# Página de inicio
def inicio(request):
    return render(request, 'inicio.html')

# Registro de usuarios
def registro_usuario(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "✅ Usuario registrado correctamente. Ya puedes iniciar sesión.")
            return redirect('login')
        else:
            messages.error(request, "❌ Verifica los errores en el formulario.")
    else:
        form = RegistroUsuarioForm()
    return render(request, 'registro.html', {'form': form})

# Login de usuarios
def login_usuario(request):
    error = ''
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            correo = form.cleaned_data['correo']
            password = form.cleaned_data['password']
            try:
                usuario = Usuario.objects.get(correo=correo)
                if usuario.check_password(password):
                    login(request, usuario)

                    # Diccionario de redirección por rol
                    redirecciones = {
                        'Coordinador Académico': 'panel_coordinador',
                        'Docente': 'panel_docente',
                        'Estudiante': 'panel_estudiante',
                        'Acudiente': 'panel_acudiente',
                        'Padre de Familia o Acudiente': 'panel_acudiente',
                    }

                    rol_usuario = usuario.rol.nombre
                    destino = redirecciones.get(rol_usuario)

                    if destino:
                        return redirect(reverse(destino))
                    else:
                        error = f"Rol no reconocido: {rol_usuario}"

                else:
                    error = "Contraseña incorrecta"
            except Usuario.DoesNotExist:
                error = "Usuario no encontrado"
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form, 'error': error})

# Paneles de usuario
def panel_docente(request):
    return HttpResponse("Panel del Docente")

def panel_estudiante(request):
    return HttpResponse("Panel del Estudiante")

# Panel del Coordinador Académico
@login_required
@user_passes_test(es_coordinador)
def panel_coordinador(request):
    return render(request, 'panel_coordinador/panel_coordinador.html')



def panel_acudiente(request):
    return HttpResponse("Panel del Acudiente")

# CRUD de Niveles
@login_required
@user_passes_test(es_coordinador)
def lista_niveles(request):
    niveles = NivelEducativo.objects.all()
    return render(request, 'panel_coordinador/nivel_list.html', {'niveles': niveles})

@login_required
@user_passes_test(es_coordinador)
def crear_nivel(request):
    if request.method == 'POST':
        form = NivelEducativoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Nivel Educativo creado correctamente.")
            return redirect('lista_niveles')
        else:
            messages.error(request, "Error al crear el nivel educativo.")
    else:
        form = NivelEducativoForm()
    return render(request, 'panel_coordinador/nivel_form.html', {'form': form})

@login_required
@user_passes_test(es_coordinador)
def editar_nivel(request, pk):
    nivel = NivelEducativo.objects.get(pk=pk)
    if request.method == 'POST':
        form = NivelEducativoForm(request.POST, instance=nivel)
        if form.is_valid():
            form.save()
            messages.success(request, "Nivel Educativo actualizado correctamente.")
            return redirect('lista_niveles')
        else:
            messages.error(request, "Error al actualizar el nivel educativo.")
    else:
        form = NivelEducativoForm(instance=nivel)
    return render(request, 'panel_coordinador/nivel_form.html', {'form': form})

@login_required
@user_passes_test(es_coordinador)
def eliminar_nivel(request, pk):
    nivel = NivelEducativo.objects.get(pk=pk)
    nivel.delete()
    messages.success(request, "Nivel Educativo eliminado correctamente.")
    return redirect('lista_niveles')

# CRUD de Grados
@login_required
@user_passes_test(es_coordinador)
def lista_grados(request):
    grados = Grado.objects.all()
    return render(request, 'panel_coordinador/grado_list.html', {'grados': grados})

@login_required
@user_passes_test(es_coordinador)
def crear_grado(request):
    if request.method == 'POST':
        form = GradoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Grado creado correctamente.")
            return redirect('lista_grados')
        else:
            messages.error(request, "Error al crear el grado.")
    else:
        form = GradoForm()
    return render(request, 'panel_coordinador/grado_form.html', {'form': form})

@login_required
@user_passes_test(es_coordinador)
def editar_grado(request, pk):
    grado = Grado.objects.get(pk=pk)
    if request.method == 'POST':
        form = GradoForm(request.POST, instance=grado)
        if form.is_valid():
            form.save()
            messages.success(request, "Grado actualizado correctamente.")
            return redirect('lista_grados')
        else:
            messages.error(request, "Error al actualizar el grado.")
    else:
        form = GradoForm(instance=grado)
    return render(request, 'panel_coordinador/grado_form.html', {'form': form})

@login_required
@user_passes_test(es_coordinador)
def eliminar_grado(request, pk):
    grado = Grado.objects.get(pk=pk)
    grado.delete()
    messages.success(request, "Grado eliminado correctamente.")
    return redirect('lista_grados')

# CRUD de Áreas
@login_required
@user_passes_test(es_coordinador)
def lista_areas(request):
    areas = Area.objects.all()
    return render(request, 'panel_coordinador/area_list.html', {'areas': areas})

@login_required
@user_passes_test(es_coordinador)
def crear_area(request):
    if request.method == 'POST':
        form = AreaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Área creada correctamente.")
            return redirect('lista_areas')
        else:
            messages.error(request, "Error al crear el área.")
    else:
        form = AreaForm()
    return render(request, 'panel_coordinador/area_form.html', {'form': form})

@login_required
@user_passes_test(es_coordinador)
def editar_area(request, pk):
    area = Area.objects.get(pk=pk)
    if request.method == 'POST':
        form = AreaForm(request.POST, instance=area)
        if form.is_valid():
            form.save()
            messages.success(request, "Área actualizada correctamente.")
            return redirect('lista_areas')
        else:
            messages.error(request, "Error al actualizar el área.")
    else:
        form = AreaForm(instance=area)
    return render(request, 'panel_coordinador/area_form.html', {'form': form})

@login_required
@user_passes_test(es_coordinador)
def eliminar_area(request, pk):
    area = Area.objects.get(pk=pk)
    area.delete()
    messages.success(request, "Área eliminada correctamente.")
    return redirect('lista_areas')

# CRUD de Asignaturas
@login_required
@user_passes_test(es_coordinador)
def lista_asignaturas(request):
    asignaturas = Asignatura.objects.all()
    return render(request, 'panel_coordinador/asignatura_list.html', {'asignaturas': asignaturas})

@login_required
@user_passes_test(es_coordinador)
def crear_asignatura(request):
    if request.method == 'POST':
        form = AsignaturaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Asignatura creada correctamente.")
            return redirect('lista_asignaturas')
        else:
            messages.error(request, "Error al crear la asignatura.")
    else:
        form = AsignaturaForm()
    return render(request, 'panel_coordinador/asignatura_form.html', {'form': form})

@login_required
@user_passes_test(es_coordinador)
def editar_asignatura(request, pk):
    asignatura = Asignatura.objects.get(pk=pk)
    if request.method == 'POST':
        form = AsignaturaForm(request.POST, instance=asignatura)
        if form.is_valid():
            form.save()
            messages.success(request, "Asignatura actualizada correctamente.")
            return redirect('lista_asignaturas')
        else:
            messages.error(request, "Error al actualizar la asignatura.")
    else:
        form = AsignaturaForm(instance=asignatura)
    return render(request, 'panel_coordinador/asignatura_form.html', {'form': form})

@login_required
@user_passes_test(es_coordinador)
def eliminar_asignatura(request, pk):
    asignatura = Asignatura.objects.get(pk=pk)
    asignatura.delete()
    messages.success(request, "Asignatura eliminada correctamente.")
    return redirect('lista_asignaturas')

# Vista para listar los temas
@login_required
@user_passes_test(es_coordinador)
def lista_temas(request):
    temas = Tema.objects.all()  # Obtiene todos los temas
    return render(request, 'panel_coordinador/tema_list.html', {'temas': temas})

# Vista para crear un nuevo tema
@login_required
@user_passes_test(es_coordinador)
def crear_tema(request):
    if request.method == 'POST':
        form = TemaForm(request.POST)  # Crea el formulario con los datos POST
        if form.is_valid():
            form.save()  # Guarda el nuevo tema en la base de datos
            messages.success(request, "Tema creado correctamente.")
            return redirect('lista_temas')  # Redirige a la lista de temas
        else:
            messages.error(request, "Error al crear el tema.")
    else:
        form = TemaForm()  # Si es GET, muestra el formulario vacío

    return render(request, 'panel_coordinador/tema_form.html', {'form': form})

# Vista para editar un tema
@login_required
@user_passes_test(es_coordinador)
def editar_tema(request, pk):
    tema = Tema.objects.get(pk=pk)  # Obtiene el tema a editar
    if request.method == 'POST':
        form = TemaForm(request.POST, instance=tema)  # Pasa el tema al formulario
        if form.is_valid():
            form.save()  # Guarda los cambios en el tema
            messages.success(request, "Tema actualizado correctamente.")
            return redirect('lista_temas')  # Redirige a la lista de temas
        else:
            messages.error(request, "Error al actualizar el tema.")
    else:
        form = TemaForm(instance=tema)  # Si es un GET, pre-carga el formulario con los datos del tema

    return render(request, 'panel_coordinador/tema_form.html', {'form': form})

# Vista para eliminar un tema
@login_required
@user_passes_test(es_coordinador)
def eliminar_tema(request, pk):
    tema = Tema.objects.get(pk=pk)  # Obtiene el tema a eliminar
    tema.delete()  # Elimina el tema de la base de datos
    messages.success(request, "Tema eliminado correctamente.")
    return redirect('lista_temas')  # Redirige a la lista de temas

# Vista para listar los logros
@login_required
@user_passes_test(es_coordinador)
def lista_logros(request):
    logros = Logro.objects.all()  # Obtiene todos los logros de la base de datos
    return render(request, 'panel_coordinador/logro_list.html', {'logros': logros})

# Vista para crear un nuevo logro
@login_required
@user_passes_test(es_coordinador)
def crear_logro(request):
    if request.method == 'POST':
        form = LogroForm(request.POST)  # Crea el formulario con los datos POST
        if form.is_valid():
            form.save()  # Guarda el nuevo logro en la base de datos
            messages.success(request, "Logro creado correctamente.")
            return redirect('lista_logros')  # Redirige a la lista de logros
        else:
            messages.error(request, "Error al crear el logro.")
    else:
        form = LogroForm()  # Si es GET, muestra el formulario vacío

    return render(request, 'panel_coordinador/logro_form.html', {'form': form})

# Vista para editar un logro
@login_required
@user_passes_test(es_coordinador)
def editar_logro(request, pk):
    logro = Logro.objects.get(pk=pk)  # Obtiene el logro a editar
    if request.method == 'POST':
        form = LogroForm(request.POST, instance=logro)  # Pasa el logro al formulario
        if form.is_valid():
            form.save()  # Guarda los cambios en el logro
            messages.success(request, "Logro actualizado correctamente.")
            return redirect('lista_logros')  # Redirige a la lista de logros
        else:
            messages.error(request, "Error al actualizar el logro.")
    else:
        form = LogroForm(instance=logro)  # Si es GET, pre-carga el formulario con los datos del logro

    return render(request, 'panel_coordinador/logro_form.html', {'form': form})

# Vista para eliminar un logro
@login_required
@user_passes_test(es_coordinador)
def eliminar_logro(request, pk):
    logro = Logro.objects.get(pk=pk)  # Obtiene el logro a eliminar
    logro.delete()  # Elimina el logro de la base de datos
    messages.success(request, "Logro eliminado correctamente.")
    return redirect('lista_logros')  # Redirige a la lista de logros
