from django.db import models

# Tablas Paramétricas
class Rol(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name = "Rol"
        verbose_name_plural = "Roles"

    def __str__(self):
        return self.nombre

class TipoDocumento(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name = "Tipo de Documento"
        verbose_name_plural = "Tipos de Documento"

    def __str__(self):
        return self.nombre

class Departamento(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = "Departamento"
        verbose_name_plural = "Departamentos"

    def __str__(self):
        return self.nombre

class Ciudad(models.Model):
    nombre = models.CharField(max_length=100)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE, related_name="ciudades")

    class Meta:
        unique_together = ('nombre', 'departamento')
        verbose_name = "Ciudad"
        verbose_name_plural = "Ciudades"

    def __str__(self):
        return f"{self.nombre} ({self.departamento})"

# Persona base
class Persona(models.Model):
    primer_nombre = models.CharField(max_length=50)
    segundo_nombre = models.CharField(max_length=50, blank=True, null=True)
    primer_apellido = models.CharField(max_length=50)
    segundo_apellido = models.CharField(max_length=50, blank=True, null=True)
    tipo_documento = models.ForeignKey(TipoDocumento, on_delete=models.PROTECT)
    numero_documento = models.CharField(max_length=20, unique=True)
    direccion_linea1 = models.CharField(max_length=100)
    direccion_linea2 = models.CharField(max_length=100, blank=True, null=True)
    ciudad = models.ForeignKey(Ciudad, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.primer_nombre} {self.segundo_nombre or ''} {self.primer_apellido} {self.segundo_apellido or ''}".strip()

class Usuario(models.Model):
    correo = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    persona = models.OneToOneField(Persona, on_delete=models.CASCADE, related_name="usuario")
    rol = models.ForeignKey(Rol, on_delete=models.PROTECT)

    def __str__(self):
        return self.correo

class Estudiante(models.Model):
    persona = models.OneToOneField(Persona, on_delete=models.CASCADE)

class Docente(models.Model):
    persona = models.OneToOneField(Persona, on_delete=models.CASCADE)
    especialidad = models.CharField(max_length=100)

class Acudiente(models.Model):
    persona = models.OneToOneField(Persona, on_delete=models.CASCADE)

class NivelEducativo(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nombre

class Grado(models.Model):
    nivel = models.ForeignKey(NivelEducativo, on_delete=models.CASCADE, related_name="grados")
    nombre = models.CharField(max_length=10)

    class Meta:
        unique_together = ('nivel', 'nombre')

    def __str__(self):
        return f"{self.nivel.nombre} - {self.nombre}"

class Area(models.Model):
    nombre = models.CharField(max_length=100)
    obligatoria = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

class Asignatura(models.Model):
    nombre = models.CharField(max_length=100)
    grado = models.ForeignKey(Grado, on_delete=models.CASCADE, related_name="asignaturas")
    area = models.ForeignKey(Area, on_delete=models.CASCADE, related_name="asignaturas")

    class Meta:
        unique_together = ('nombre', 'grado', 'area')

    def __str__(self):
        return self.nombre

class Tema(models.Model):
    asignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE, related_name="temas")
    nombre = models.CharField(max_length=100)

class Logro(models.Model):
    asignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE, related_name="logros")
    descripcion = models.TextField()

class Aula(models.Model):
    ESTADOS = [
        ('Disponible', 'Disponible'),
        ('Ocupada', 'Ocupada'),
        ('Mantenimiento', 'Mantenimiento')
    ]
    nombre = models.CharField(max_length=50)
    capacidad = models.PositiveIntegerField()
    estado = models.CharField(max_length=20, choices=ESTADOS, default='Disponible')

    def __str__(self):
        return self.nombre

class Grupo(models.Model):
    grado = models.ForeignKey(Grado, on_delete=models.CASCADE, related_name="grupos")
    nombre = models.CharField(max_length=10)
    aula = models.ForeignKey(Aula, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.nombre} ({self.grado})"

class AsignacionDocente(models.Model):
    docente = models.ForeignKey(Docente, on_delete=models.CASCADE)
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE)
    asignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('docente', 'grupo', 'asignatura')

class Actividad(models.Model):
    asignacion = models.ForeignKey(AsignacionDocente, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    es_calificable = models.BooleanField(default=True)
    fecha_publicacion = models.DateField(auto_now_add=True)

class Calificacion(models.Model):
    actividad = models.ForeignKey(Actividad, on_delete=models.CASCADE)
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    nota = models.DecimalField(max_digits=3, decimal_places=1)
    fecha_registro = models.DateField(auto_now_add=True)
