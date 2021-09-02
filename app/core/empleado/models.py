from django.db import models
from core.persona.models import Persona


class Puesto(models.Model):
    id_puesto = models.IntegerField(db_column='ID_PUESTO', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='NOMBRE', max_length=50)  # Field name made lowercase.
    requisitos = models.CharField(db_column='REQUISITOS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='DESCRIPCION', max_length=255, blank=True, null=True)  # Field name made lowercase.
    salario = models.DecimalField(db_column='SALARIO', max_digits=7, decimal_places=2)  # Field name made lowercase.
    horario_entrada = models.TimeField(db_column='HORARIO_ENTRADA')  # Field name made lowercase.
    horario_salida = models.TimeField(db_column='HORARIO_SALIDA')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'puesto'


class Empleado(models.Model):
    cod_empleado = models.IntegerField(db_column='COD_EMPLEADO', primary_key=True)  # Field name made lowercase.
    pass_field = models.CharField(db_column='PASS', max_length=64)  # Field name made lowercase. Field renamed because it was a Python reserved word.
    persona = models.ForeignKey(Persona, models.DO_NOTHING, db_column='PERSONA_ID')  # Field name made lowercase.
    correo = models.CharField(db_column='CORREO', max_length=100, blank=True, null=True)  # Field name made lowercase.
    puesto = models.ForeignKey(Puesto, models.DO_NOTHING, db_column='PUESTO_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'empleado'