from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'index.html')

#def contacto(request):
#    return render(request, 'miapp/contacto.html')

#def productos(request):
#    return render(request, 'miapp/productos.html')

