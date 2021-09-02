from django.db import models
from core.sucursal.models import Sucursal
from core.proveedor.models import Proveedor


class Marca(models.Model):
    id_marca = models.IntegerField(db_column='ID_MARCA', primary_key=True)  # Field name made lowercase.
    marca = models.CharField(db_column='MARCA', max_length=35)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'marca'


class Producto(models.Model):
    cod_producto = models.CharField(db_column='COD_PRODUCTO', primary_key=True, max_length=25)  # Field name made lowercase.
    nombre = models.CharField(db_column='NOMBRE', max_length=35)  # Field name made lowercase.
    descripcion = models.CharField(db_column='DESCRIPCION', max_length=255, blank=True, null=True)  # Field name made lowercase.
    porcentaje_ganancia = models.DecimalField(db_column='PORCENTAJE_GANANCIA', max_digits=4, decimal_places=2)  # Field name made lowercase.
    precio_venta = models.DecimalField(db_column='PRECIO_VENTA', max_digits=7, decimal_places=2)  # Field name made lowercase.
    fecha_agregado = models.DateField(db_column='FECHA_AGREGADO')  # Field name made lowercase.
    fecha_vencimiento = models.DateField(db_column='FECHA_VENCIMIENTO')  # Field name made lowercase.
    recien_ingreso = models.CharField(db_column='RECIEN_INGRESO', max_length=1)  # Field name made lowercase.
    cantidad = models.IntegerField(db_column='CANTIDAD')  # Field name made lowercase.
    marca = models.ForeignKey(Marca, models.DO_NOTHING, db_column='MARCA_ID')  # Field name made lowercase.
    sucursal = models.ForeignKey(Sucursal, models.DO_NOTHING, db_column='SUCURSAL_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'producto'


class DetalleProducto(models.Model):
    id_detalle_producto = models.IntegerField(db_column='ID_DETALLE_PRODUCTO', primary_key=True)  # Field name made lowercase.
    proveedor = models.ForeignKey(Proveedor, models.DO_NOTHING, db_column='PROVEEDOR_ID')  # Field name made lowercase.
    producto_cod = models.ForeignKey(Producto, models.DO_NOTHING, db_column='PRODUCTO_COD')  # Field name made lowercase.
    precio_costo = models.DecimalField(db_column='PRECIO_COSTO', max_digits=7, decimal_places=2)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'detalle_producto'