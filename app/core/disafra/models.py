# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Categoria(models.Model):
    id_categoria = models.AutoField(db_column='ID_CATEGORIA', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='NOMBRE', max_length=35)  # Field name made lowercase.
    descripcion = models.CharField(db_column='DESCRIPCION', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'categoria'


class Cliente(models.Model):
    nit_cliente = models.CharField(db_column='NIT_CLIENTE', primary_key=True, max_length=15)  # Field name made lowercase.
    persona = models.ForeignKey('Persona', models.DO_NOTHING, db_column='PERSONA_ID')  # Field name made lowercase.
    mayorista = models.CharField(db_column='MAYORISTA', max_length=1)  # Field name made lowercase.
    correo = models.ForeignKey('UsuarioCliente', models.DO_NOTHING, db_column='CORREO')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cliente'


class Compra(models.Model):
    num_compra = models.AutoField(db_column='NUM_COMPRA', primary_key=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='DESCRIPCION', max_length=255, blank=True, null=True)  # Field name made lowercase.
    total = models.DecimalField(db_column='TOTAL', max_digits=7, decimal_places=2)  # Field name made lowercase.
    total_pagado = models.DecimalField(db_column='TOTAL_PAGADO', max_digits=7, decimal_places=2)  # Field name made lowercase.
    pagado = models.CharField(db_column='PAGADO', max_length=1)  # Field name made lowercase.
    fecha_compra = models.DateField(db_column='FECHA_COMPRA')  # Field name made lowercase.
    entregado = models.CharField(db_column='ENTREGADO', max_length=1)  # Field name made lowercase.
    fecha_entregado = models.DateField(db_column='FECHA_ENTREGADO')  # Field name made lowercase.
    visitador = models.ForeignKey('Visitador', models.DO_NOTHING, db_column='VISITADOR_ID')  # Field name made lowercase.
    empleado_cod = models.ForeignKey('Empleado', models.DO_NOTHING, db_column='EMPLEADO_COD')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'compra'


class Cotizacion(models.Model):
    num_cotizacion = models.AutoField(db_column='NUM_COTIZACION', primary_key=True)  # Field name made lowercase.
    cliente_nit = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='CLIENTE_NIT')  # Field name made lowercase.
    empleado_cod = models.ForeignKey('Empleado', models.DO_NOTHING, db_column='EMPLEADO_COD')  # Field name made lowercase.
    sucursal = models.ForeignKey('Sucursal', models.DO_NOTHING, db_column='SUCURSAL_ID')  # Field name made lowercase.
    fecha_venta = models.DateField(db_column='FECHA_VENTA')  # Field name made lowercase.
    total = models.DecimalField(db_column='TOTAL', max_digits=7, decimal_places=2)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cotizacion'


class Departamento(models.Model):
    id_departamento = models.AutoField(db_column='ID_DEPARTAMENTO', primary_key=True)  # Field name made lowercase.
    departamento = models.CharField(db_column='DEPARTAMENTO', max_length=25, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'departamento'


class Descuento(models.Model):
    cod_descuento = models.CharField(db_column='COD_DESCUENTO', primary_key=True, max_length=25)  # Field name made lowercase.
    porcentaje = models.DecimalField(db_column='PORCENTAJE', max_digits=4, decimal_places=2)  # Field name made lowercase.
    descripcion = models.CharField(db_column='DESCRIPCION', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'descuento'


class DetalleCompra(models.Model):
    id_detalle_compra = models.AutoField(db_column='ID_DETALLE_COMPRA', primary_key=True)  # Field name made lowercase.
    detalle_producto = models.ForeignKey('DetalleProducto', models.DO_NOTHING, db_column='DETALLE_PRODUCTO_ID')  # Field name made lowercase.
    cantidad = models.IntegerField(db_column='CANTIDAD')  # Field name made lowercase.
    subtotal = models.DecimalField(db_column='SUBTOTAL', max_digits=7, decimal_places=2)  # Field name made lowercase.
    compra_num = models.ForeignKey(Compra, models.DO_NOTHING, db_column='COMPRA_NUM')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'detalle_compra'


class DetalleCotizacion(models.Model):
    id_detalle_cotizacion = models.AutoField(db_column='ID_DETALLE_COTIZACION', primary_key=True)  # Field name made lowercase.
    producto_cod = models.ForeignKey('Producto', models.DO_NOTHING, db_column='PRODUCTO_COD', blank=True, null=True)  # Field name made lowercase.
    cotizacion_num = models.ForeignKey(Cotizacion, models.DO_NOTHING, db_column='COTIZACION_NUM')  # Field name made lowercase.
    descuento_cod = models.ForeignKey(Descuento, models.DO_NOTHING, db_column='DESCUENTO_COD', blank=True, null=True)  # Field name made lowercase.
    cantidad = models.IntegerField(db_column='CANTIDAD')  # Field name made lowercase.
    subtotal = models.DecimalField(db_column='SUBTOTAL', max_digits=7, decimal_places=2)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'detalle_cotizacion'


class DetalleProducto(models.Model):
    id_detalle_producto = models.AutoField(db_column='ID_DETALLE_PRODUCTO', primary_key=True)  # Field name made lowercase.
    proveedor = models.ForeignKey('Proveedor', models.DO_NOTHING, db_column='PROVEEDOR_ID')  # Field name made lowercase.
    producto_cod = models.ForeignKey('Producto', models.DO_NOTHING, db_column='PRODUCTO_COD')  # Field name made lowercase.
    precio_costo = models.DecimalField(db_column='PRECIO_COSTO', max_digits=7, decimal_places=2)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'detalle_producto'


class DetalleVenta(models.Model):
    id_detalle_venta = models.AutoField(db_column='ID_DETALLE_VENTA', primary_key=True)  # Field name made lowercase.
    producto_cod = models.ForeignKey('Producto', models.DO_NOTHING, db_column='PRODUCTO_COD', blank=True, null=True)  # Field name made lowercase.
    venta_num = models.ForeignKey('Venta', models.DO_NOTHING, db_column='VENTA_NUM')  # Field name made lowercase.
    descuento_cod = models.ForeignKey(Descuento, models.DO_NOTHING, db_column='DESCUENTO_COD', blank=True, null=True)  # Field name made lowercase.
    cantidad = models.IntegerField(db_column='CANTIDAD')  # Field name made lowercase.
    subtotal = models.DecimalField(db_column='SUBTOTAL', max_digits=7, decimal_places=2)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'detalle_venta'


class Direccion(models.Model):
    id_direccion = models.AutoField(db_column='ID_DIRECCION', primary_key=True)  # Field name made lowercase.
    direccion = models.CharField(db_column='DIRECCION', max_length=150)  # Field name made lowercase.
    referencia = models.CharField(db_column='REFERENCIA', max_length=150, blank=True, null=True)  # Field name made lowercase.
    municipio = models.ForeignKey('Municipio', models.DO_NOTHING, db_column='MUNICIPIO_ID')  # Field name made lowercase.
    persona = models.ForeignKey('Persona', models.DO_NOTHING, db_column='PERSONA_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'direccion'


class Empleado(models.Model):
    cod_empleado = models.AutoField(db_column='COD_EMPLEADO', primary_key=True)  # Field name made lowercase.
    pass_field = models.CharField(db_column='PASS', max_length=64)  # Field name made lowercase. Field renamed because it was a Python reserved word.
    persona = models.ForeignKey('Persona', models.DO_NOTHING, db_column='PERSONA_ID')  # Field name made lowercase.
    correo = models.CharField(db_column='CORREO', max_length=100, blank=True, null=True)  # Field name made lowercase.
    puesto = models.ForeignKey('Puesto', models.DO_NOTHING, db_column='PUESTO_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'empleado'


class Marca(models.Model):
    id_marca = models.AutoField(db_column='ID_MARCA', primary_key=True)  # Field name made lowercase.
    marca = models.CharField(db_column='MARCA', max_length=35)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'marca'


class Municipio(models.Model):
    id_municipio = models.AutoField(db_column='ID_MUNICIPIO', primary_key=True)  # Field name made lowercase.
    municipio = models.CharField(db_column='MUNICIPIO', max_length=35)  # Field name made lowercase.
    departamento = models.ForeignKey(Departamento, models.DO_NOTHING, db_column='DEPARTAMENTO_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'municipio'


class PagoCompra(models.Model):
    num_pago = models.IntegerField(db_column='NUM_PAGO', primary_key=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='DESCRIPCION', max_length=255, blank=True, null=True)  # Field name made lowercase.
    fecha_pago = models.DateField(db_column='FECHA_PAGO')  # Field name made lowercase.
    cantidad_pagada = models.DecimalField(db_column='CANTIDAD_PAGADA', max_digits=7, decimal_places=2)  # Field name made lowercase.
    empleado_cod = models.ForeignKey(Empleado, models.DO_NOTHING, db_column='EMPLEADO_COD')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pago_compra'


class Persona(models.Model):
    id_persona = models.AutoField(db_column='ID_PERSONA', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='NOMBRE', max_length=50)  # Field name made lowercase.
    apellido = models.CharField(db_column='APELLIDO', max_length=50)  # Field name made lowercase.
    fecha_nacimiento = models.DateField(db_column='FECHA_NACIMIENTO')  # Field name made lowercase.
    edad = models.IntegerField(db_column='EDAD')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'persona'


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
    sucursal = models.ForeignKey('Sucursal', models.DO_NOTHING, db_column='SUCURSAL_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'producto'


class Proveedor(models.Model):
    id_proveedor = models.AutoField(db_column='ID_PROVEEDOR', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='NOMBRE', max_length=35)  # Field name made lowercase.
    correo = models.CharField(db_column='CORREO', max_length=100)  # Field name made lowercase.
    direccion = models.ForeignKey(Direccion, models.DO_NOTHING, db_column='DIRECCION_ID')  # Field name made lowercase.
    telefono = models.ForeignKey('Telefono', models.DO_NOTHING, db_column='TELEFONO_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'proveedor'


class Puesto(models.Model):
    id_puesto = models.AutoField(db_column='ID_PUESTO', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='NOMBRE', max_length=50)  # Field name made lowercase.
    requisitos = models.CharField(db_column='REQUISITOS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='DESCRIPCION', max_length=255, blank=True, null=True)  # Field name made lowercase.
    salario = models.DecimalField(db_column='SALARIO', max_digits=7, decimal_places=2)  # Field name made lowercase.
    horario_entrada = models.TimeField(db_column='HORARIO_ENTRADA')  # Field name made lowercase.
    horario_salida = models.TimeField(db_column='HORARIO_SALIDA')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'puesto'


class SubCategoria(models.Model):
    id_sub_categoria = models.AutoField(db_column='ID_SUB_CATEGORIA', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='NOMBRE', max_length=35)  # Field name made lowercase.
    categoria = models.ForeignKey(Categoria, models.DO_NOTHING, db_column='CATEGORIA_ID')  # Field name made lowercase.
    producto_cod = models.ForeignKey(Producto, models.DO_NOTHING, db_column='PRODUCTO_COD')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sub_categoria'


class Sucursal(models.Model):
    id_sucursal = models.AutoField(db_column='ID_SUCURSAL', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='NOMBRE', max_length=35)  # Field name made lowercase.
    correo = models.CharField(db_column='CORREO', max_length=100)  # Field name made lowercase.
    direccion = models.ForeignKey(Direccion, models.DO_NOTHING, db_column='DIRECCION_ID')  # Field name made lowercase.
    telefono = models.ForeignKey('Telefono', models.DO_NOTHING, db_column='TELEFONO_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sucursal'


class Telefono(models.Model):
    id_telefono = models.AutoField(db_column='ID_TELEFONO', primary_key=True)  # Field name made lowercase.
    numero = models.CharField(db_column='NUMERO', max_length=16)  # Field name made lowercase.
    tipo_telefono = models.ForeignKey('TipoTelefono', models.DO_NOTHING, db_column='TIPO_TELEFONO_ID')  # Field name made lowercase.
    extension = models.CharField(db_column='EXTENSION', max_length=5, blank=True, null=True)  # Field name made lowercase.
    persona = models.ForeignKey(Persona, models.DO_NOTHING, db_column='PERSONA_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'telefono'


class TipoTelefono(models.Model):
    id_tipo_telefono = models.AutoField(db_column='ID_TIPO_TELEFONO', primary_key=True)  # Field name made lowercase.
    tipo = models.CharField(db_column='TIPO', max_length=15, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tipo_telefono'


class UsuarioCliente(models.Model):
    correo = models.CharField(db_column='CORREO', primary_key=True, max_length=100)  # Field name made lowercase.
    pass_field = models.CharField(db_column='PASS', max_length=64)  # Field name made lowercase. Field renamed because it was a Python reserved word.
    activo = models.CharField(db_column='ACTIVO', max_length=1)  # Field name made lowercase.
    fecha_creado = models.DateField(db_column='FECHA_CREADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'usuario_cliente'


class UsuarioSucursal(models.Model):
    usuario = models.CharField(db_column='USUARIO', primary_key=True, max_length=50)  # Field name made lowercase.
    pass_field = models.CharField(db_column='PASS', max_length=64)  # Field name made lowercase. Field renamed because it was a Python reserved word.
    activo = models.CharField(db_column='ACTIVO', max_length=1)  # Field name made lowercase.
    fecha_creado = models.DateField(db_column='FECHA_CREADO', blank=True, null=True)  # Field name made lowercase.
    sucursal = models.ForeignKey(Sucursal, models.DO_NOTHING, db_column='SUCURSAL_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'usuario_sucursal'


class Venta(models.Model):
    num_venta = models.AutoField(db_column='NUM_VENTA', primary_key=True)  # Field name made lowercase.
    cliente_nit = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='CLIENTE_NIT')  # Field name made lowercase.
    empleado_cod = models.ForeignKey(Empleado, models.DO_NOTHING, db_column='EMPLEADO_COD')  # Field name made lowercase.
    sucursal = models.ForeignKey(Sucursal, models.DO_NOTHING, db_column='SUCURSAL_ID')  # Field name made lowercase.
    fecha_venta = models.DateField(db_column='FECHA_VENTA')  # Field name made lowercase.
    total = models.DecimalField(db_column='TOTAL', max_digits=7, decimal_places=2)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'venta'


class Visitador(models.Model):
    id_visitador = models.AutoField(db_column='ID_VISITADOR', primary_key=True)  # Field name made lowercase.
    persona = models.ForeignKey(Persona, models.DO_NOTHING, db_column='PERSONA_ID')  # Field name made lowercase.
    proveedor = models.ForeignKey(Proveedor, models.DO_NOTHING, db_column='PROVEEDOR_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'visitador'
