from django.shortcuts import render, redirect
from .forms import RegistroUsuarioForm

def login(request):
    return render(request, 'login.html')


def registro_usuario(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = RegistroUsuarioForm()
    return render(request, 'registro.html', )

#from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'index.html')

