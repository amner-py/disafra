from django.db import models
from core.direccion.models import Direccion
from core.telefono.models import Telefono


class Sucursal(models.Model):
    id_sucursal = models.IntegerField(db_column='ID_SUCURSAL', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='NOMBRE', max_length=35)  # Field name made lowercase.
    correo = models.CharField(db_column='CORREO', max_length=100)  # Field name made lowercase.
    direccion = models.ForeignKey(Direccion, on_delete=models.CASCADE, db_column='DIRECCION_ID')  # Field name made lowercase.
    telefono_num = models.ForeignKey(Telefono, on_delete=models.CASCADE, db_column='TELEFONO_NUM')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sucursal'


class UsuarioSucursal(models.Model):
    usuario_sucursal = models.CharField(db_column='USUARIO_SUCURSAL', primary_key=True, max_length=50)  # Field name made lowercase.
    pass_field = models.CharField(db_column='PASS', max_length=64)  # Field name made lowercase. Field renamed because it was a Python reserved word.
    activo = models.BooleanField(db_column='ACTIVO')  # Field name made lowercase.
    fecha_creado = models.DateField(db_column='FECHA_CREADO', blank=True, null=True)  # Field name made lowercase.
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE, db_column='SUCURSAL_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'usuario_sucursal'


class Permiso(models.Model):
    permiso = models.CharField(db_column='PERMISO', primary_key=True, max_length=30)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'permiso'


class PermisoUsuarioSucursal(models.Model):
    id_permiso_usuario_sucursal = models.IntegerField(db_column='ID_PERMISO_USUARIO_SUCURSAL', primary_key=True)  # Field name made lowercase.
    sucursal_usuario = models.ForeignKey(UsuarioSucursal, on_delete=models.CASCADE, db_column='SUCURSAL_USUARIO')  # Field name made lowercase.
    permiso = models.ForeignKey(Permiso, on_delete=models.CASCADE, db_column='PERMISO')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'permiso_usuario_sucursal'