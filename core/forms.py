from django import forms
from .models import Usuario, Rol
from django.contrib.auth.hashers import make_password
class RegistroUsuarioForm(forms.ModelForm):
    password = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput,
        help_text="Debe tener al menos 8 caracteres, incluir mayúsculas, minúsculas, un número y un símbolo especial (#$%!)"
    )
    class Meta:
        model = Usuario
        fields = ['correo', 'password', 'rol', 'persona']

    def clean_password(self):
        password = self.cleaned_data.get('password')
        # Aquí puedes agregar validaciones adicionales si lo deseas
        return make_password(password)
