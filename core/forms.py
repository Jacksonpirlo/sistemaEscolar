from django import forms
from django.contrib.auth.hashers import make_password
from .models import Usuario, Rol, NivelEducativo, Grado, Area, Asignatura, Tema, Logro
import re

# Formulario de Registro de Usuario
class RegistroUsuarioForm(forms.ModelForm):
    password = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput,
        help_text="Debe tener al menos 8 caracteres, incluir una mayúscula, una minúscula, un número y un símbolo (#$%!)."
    )
    confirmar_password = forms.CharField(
        label="Confirmar Contraseña",
        widget=forms.PasswordInput
    )

    class Meta:
        model = Usuario
        fields = ['correo', 'rol', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirmar = cleaned_data.get("confirmar_password")

        if password != confirmar:
            raise forms.ValidationError("⚠️ Las contraseñas no coinciden.")
        if len(password) < 8:
            raise forms.ValidationError("🔒 La contraseña debe tener al menos 8 caracteres.")
        if not re.search(r'[A-Z]', password):
            raise forms.ValidationError("🔒 La contraseña debe incluir al menos una letra mayúscula.")
        if not re.search(r'[a-z]', password):
            raise forms.ValidationError("🔒 La contraseña debe incluir al menos una letra minúscula.")
        if not re.search(r'\d', password):
            raise forms.ValidationError("🔒 La contraseña debe incluir al menos un número.")
        if not re.search(r'[#\$%!_]', password):
            raise forms.ValidationError("🔒 La contraseña debe incluir al menos un símbolo especial: # $ % ! _")

        return cleaned_data

    def save(self, commit=True):
        usuario = super().save(commit=False)
        usuario.set_password(self.cleaned_data["password"])
        if commit:
            usuario.save()
        return usuario

# Formulario de Login de Usuario
class LoginForm(forms.Form):
    correo = forms.EmailField(label="Correo electrónico")
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput)

# Formulario para Nivel Educativo
class NivelEducativoForm(forms.ModelForm):
    class Meta:
        model = NivelEducativo
        fields = ['nombre']

# Formulario para Grado
class GradoForm(forms.ModelForm):
    class Meta:
        model = Grado
        fields = ['nivel', 'nombre']

# Formulario para Área
class AreaForm(forms.ModelForm):
    class Meta:
        model = Area
        fields = ['nombre', 'obligatoria']

# Formulario para Asignatura
class AsignaturaForm(forms.ModelForm):
    class Meta:
        model = Asignatura
        fields = ['nombre', 'grado', 'area']

# Formulario para Tema
class TemaForm(forms.ModelForm):
    class Meta:
        model = Tema
        fields = ['nombre', 'asignatura']

# Formulario para Logro
class LogroForm(forms.ModelForm):
    class Meta:
        model = Logro
        fields = ['descripcion', 'asignatura']
