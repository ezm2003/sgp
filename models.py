# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Actividad(models.Model):
    id_actividad = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    fecha_inicio = models.DateField(blank=True, null=True)
    fecha_fin = models.DateField(blank=True, null=True)
    fk_proyecto = models.ForeignKey('Proyecto', models.DO_NOTHING, db_column='fk_proyecto', blank=True, null=True)
    fk_estado = models.ForeignKey('Estado', models.DO_NOTHING, db_column='fk_estado', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'actividad'


class Aplicacion(models.Model):
    id_aplicacion = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'aplicacion'


class Archivo(models.Model):
    id_archivo = models.AutoField(primary_key=True)
    ruta = models.TextField(blank=True, null=True)
    fk_proyecto = models.ForeignKey('Proyecto', models.DO_NOTHING, db_column='fk_proyecto', blank=True, null=True)
    fk_actividad = models.ForeignKey(Actividad, models.DO_NOTHING, db_column='fk_actividad', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'archivo'


class Area(models.Model):
    id_area = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'area'


class AreaProyecto(models.Model):
    id_area_proyecto = models.AutoField(primary_key=True)
    fk_area = models.ForeignKey(Area, models.DO_NOTHING, db_column='fk_area', blank=True, null=True)
    fk_proyecto = models.ForeignKey('Proyecto', models.DO_NOTHING, db_column='fk_proyecto', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'area_proyecto'


class Comentarios(models.Model):
    id_comentarios = models.AutoField(primary_key=True)
    fecha_creacion = models.DateTimeField(blank=True, null=True)
    fk_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='fk_usuario', blank=True, null=True)
    fk_tarea = models.ForeignKey(Actividad, models.DO_NOTHING, db_column='fk_tarea', blank=True, null=True)
    contenido = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'comentarios'


class Estado(models.Model):
    id_estado = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'estado'


class EstadoActividad(models.Model):
    id_estado_actividad = models.AutoField(primary_key=True)
    fk_estado = models.ForeignKey(Estado, models.DO_NOTHING, db_column='fk_estado', blank=True, null=True)
    fk_actividad = models.ForeignKey(Actividad, models.DO_NOTHING, db_column='fk_actividad', blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'estado_actividad'


class EstadoProyecto(models.Model):
    id_estado_proyecto = models.AutoField(primary_key=True)
    fk_estado = models.ForeignKey(Estado, models.DO_NOTHING, db_column='fk_estado', blank=True, null=True)
    fk_proyecto = models.ForeignKey('Proyecto', models.DO_NOTHING, db_column='fk_proyecto', blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'estado_proyecto'


class Etiqueta(models.Model):
    id_etiqueta = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'etiqueta'


class EtiquetaActividad(models.Model):
    id_etiqueta_actividad = models.AutoField(primary_key=True)
    fk_etiqueta = models.ForeignKey(Etiqueta, models.DO_NOTHING, db_column='fk_etiqueta', blank=True, null=True)
    fk_actividad = models.ForeignKey(Actividad, models.DO_NOTHING, db_column='fk_actividad', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'etiqueta_actividad'


class Msgerror(models.Model):
    uniqueid = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'msgerror'


class Notificacion(models.Model):
    id_notificacion = models.AutoField(primary_key=True)
    fecha = models.DateTimeField(blank=True, null=True)
    contenido = models.TextField(blank=True, null=True)
    fk_actividad = models.ForeignKey(Actividad, models.DO_NOTHING, db_column='fk_actividad', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'notificacion'


class Persona(models.Model):
    id_persona = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    apellidos = models.CharField(max_length=200, blank=True, null=True)
    codigo = models.CharField(max_length=25, blank=True, null=True)
    documento = models.CharField(max_length=25, blank=True, null=True)
    avatar = models.CharField(max_length=200, blank=True, null=True)
    numero = models.CharField(max_length=25, blank=True, null=True)
    email = models.CharField(unique=True, max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'persona'


class Proyecto(models.Model):
    id_proyecto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    fecha_inicio = models.DateField(blank=True, null=True)
    fecha_fin = models.DateField(blank=True, null=True)
    fk_estado = models.ForeignKey(Estado, models.DO_NOTHING, db_column='fk_estado', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'proyecto'


class ProyectoUsuario(models.Model):
    id_proy_usuario = models.AutoField(primary_key=True)
    email = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='email', blank=True, null=True)
    fk_proyecto = models.ForeignKey(Proyecto, models.DO_NOTHING, db_column='fk_proyecto', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'proyecto_usuario'


class Rol(models.Model):
    id_rol = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rol'


class RolUsuarioAplicacion(models.Model):
    id_rol_usuario_aplicacion = models.AutoField(primary_key=True)
    fk_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='fk_usuario', blank=True, null=True)
    fk_rol = models.ForeignKey(Rol, models.DO_NOTHING, db_column='fk_rol', blank=True, null=True)
    fk_aplicacion = models.ForeignKey(Aplicacion, models.DO_NOTHING, db_column='fk_aplicacion', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rol_usuario_aplicacion'


class Tipo(models.Model):
    id_tipo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipo'


class TipoProyecto(models.Model):
    id_tipo_proyecto = models.AutoField(primary_key=True)
    fk_tipo = models.ForeignKey(Tipo, models.DO_NOTHING, db_column='fk_tipo', blank=True, null=True)
    fk_proyecto = models.ForeignKey(Proyecto, models.DO_NOTHING, db_column='fk_proyecto', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipo_proyecto'


class Usuario(models.Model):
    email = models.CharField(primary_key=True, max_length=100)
    contrasena = models.CharField(max_length=255, blank=True, null=True)
    id_persona = models.ForeignKey(Persona, models.DO_NOTHING, db_column='id_persona', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usuario'
