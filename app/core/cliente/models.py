from django.db import models
from core.persona.models import Persona


class UsuarioCliente(models.Model):
    correo = models.CharField(db_column='CORREO', primary_key=True, max_length=100)  # Field name made lowercase.
    pass_field = models.CharField(db_column='PASS', max_length=64)  # Field name made lowercase. Field renamed because it was a Python reserved word.
    activo = models.BooleanField(db_column='ACTIVO')  # Field name made lowercase.
    fecha_creado = models.DateField(db_column='FECHA_CREADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'usuario_cliente'
        verbose_name = 'Usuario de Cliente'
        verbose_name_plural = 'Usuarios de Cliente'


class Cliente(models.Model):
    nit_cliente = models.CharField(db_column='NIT_CLIENTE', primary_key=True, max_length=15)  # Field name made lowercase.
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE, db_column='PERSONA_ID')  # Field name made lowercase.
    mayorista = models.BooleanField(db_column='MAYORISTA')  # Field name made lowercase.
    correo = models.ForeignKey(UsuarioCliente, on_delete=models.CASCADE, db_column='CORREO')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cliente'
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'