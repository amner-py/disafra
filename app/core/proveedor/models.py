from django.db import models
from core.persona.models import Persona
from core.direccion.models import Direccion
from core.telefono.models import Telefono


class Proveedor(models.Model):
    id_proveedor = models.IntegerField(db_column='ID_PROVEEDOR', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='NOMBRE', max_length=35)  # Field name made lowercase.
    correo = models.CharField(db_column='CORREO', max_length=100)  # Field name made lowercase.
    direccion = models.ForeignKey(Direccion, on_delete=models.CASCADE, db_column='DIRECCION_ID')  # Field name made lowercase.
    telefono_num = models.ForeignKey(Telefono, on_delete=models.CASCADE, db_column='TELEFONO_NUM')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'proveedor'
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'


class Visitador(models.Model):
    id_visitador = models.IntegerField(db_column='ID_VISITADOR', primary_key=True)  # Field name made lowercase.
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE, db_column='PERSONA_ID')  # Field name made lowercase.
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE, db_column='PROVEEDOR_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'visitador'
        verbose_name = 'Visitador'
        verbose_name_plural = 'Visitadores'