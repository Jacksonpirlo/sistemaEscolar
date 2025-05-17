from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),  # 👈 Esto hace que las rutas de core estén en la raíz
]
