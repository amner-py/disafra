# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

#-------------------------------Modelos-Clases--------------------------------------#

#------------------------------------Clase para tabla auth_venta------------------------------------------
class AuthVenta(models.Model):
	#Atributos de tabla
    id_auth = models.AutoField(primary_key=True)
    rango_valor_inicial = models.IntegerField()
    rango_valor_final = models.IntegerField()
    serie = models.CharField(max_length=3)


    #Clase para metadatos
    class Meta:
        managed = False
        db_table = 'auth_venta'
        verbose_name = 'Autorización de Venta'
        verbose_name_plural = 'Autorizaciones de Venta'

#------------------------------------Clase para tabla categoria-------------------------------------------
class Categoria(models.Model):
	#Atributos de tabla
    id_categoria = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=25)

    #Clase para metadatos
    class Meta:
        managed = False
        db_table = 'categoria'
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

#------------------------------------Clase para tabla cliente---------------------------------------------
class Cliente(models.Model):
	#Atributos de tabla
    nit_cliente = models.CharField(primary_key=True, max_length=13)
    persona = models.ForeignKey('Persona', models.DO_NOTHING)

    #Clase para metadatos
    class Meta:
        managed = False
        db_table = 'cliente'
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

#------------------------------------Clase para tabla compra----------------------------------------------
class Compra(models.Model):
	#Atributos de tabla
    num_compra = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=40, blank=True, null=True)
    total = models.FloatField()
    total_pagado = models.FloatField(blank=True, null=True)
    pagado = models.IntegerField()
    empleado_cod = models.ForeignKey('Empleado', models.DO_NOTHING, db_column='empleado_cod')
    pago_compra_id = models.IntegerField()
    fecha_entrega = models.DateField(blank=True, null=True)
    contacto_proveedor = models.ForeignKey('ContactoProveedor', models.DO_NOTHING)

    #Clase para metadatos
    class Meta:
        managed = False
        db_table = 'compra'
        verbose_name = 'Compra'
        verbose_name_plural = 'Compras'

#------------------------------------Clase para tabla proveedor---------------------------------------------
class ContactoProveedor(models.Model):
	#Atributos de tabla
    id_contacto_proveedor = models.AutoField(primary_key=True)
    persona = models.ForeignKey('Persona', models.DO_NOTHING)
    proveedor = models.ForeignKey('Proveedor', models.DO_NOTHING)

    #Clase para metadatos
    class Meta:
        managed = False
        db_table = 'contacto_proveedor'
        verbose_name = 'Contacto de Proveedor'
        verbose_name_plural = 'Contactos de Proveedor'

#------------------------------------Clase para tabla descuento---------------------------------------------
class Descuento(models.Model):
	#Atributos de tabla
    cod_descuento = models.CharField(primary_key=True, max_length=25)
    descripcion = models.CharField(max_length=40)
    porcentaje = models.IntegerField()

    #Clase para metadatos
    class Meta:
        managed = False
        db_table = 'descuento'
        verbose_name = 'Descuento'
        verbose_name_plural = 'Descuentos'

#------------------------------------Clase para tabla detalle_compra-----------------------------------------
class DetalleCompra(models.Model):
	#Atributos de tabla
    id_detalle_compra = models.AutoField(primary_key=True)
    compra_num = models.ForeignKey(Compra, models.DO_NOTHING, db_column='compra_num')
    detalle_producto_id = models.ForeignKey('DetalleProducto', models.DO_NOTHING, db_column='detalle_producto_id')
    cantidad = models.IntegerField()
    subtotal = models.FloatField()

    #Clase para metadatos
    class Meta:
        managed = False
        db_table = 'detalle_compra'
        verbose_name = 'Detalle de Compra'
        verbose_name_plural = 'Detalles de Compra'

#------------------------------------Clase para tabla detalle_proveedor--------------------------------------
class DetalleProducto(models.Model):
	#Atributos de tabla
    id_detalle_producto = models.AutoField(primary_key=True)
    producto = models.ForeignKey('Producto', models.DO_NOTHING, db_column='producto_cod')
    proveedor = models.ForeignKey('Proveedor', models.DO_NOTHING)



    #Clase para metadatos
    class Meta:
        managed = False
        db_table = 'detalle_producto'
        verbose_name = 'Detalle de Producto'
        verbose_name_plural = 'Detalles de Producto'

#------------------------------------Clase para tabla detalle_venta------------------------------------------
class DetalleVenta(models.Model):
	#Atributos de tabla
    id_detalle_venta = models.AutoField(primary_key=True)
    cantidad = models.IntegerField()
    sub_total = models.FloatField(blank=True, null=True)
    producto_cod = models.ForeignKey('Producto', models.DO_NOTHING, db_column='producto_cod', blank=True, null=True)
    venta_num = models.ForeignKey('Venta', models.DO_NOTHING, db_column='venta_num')
    descuento_cod = models.ForeignKey(Descuento, models.DO_NOTHING, db_column='descuento_cod', blank=True, null=True)

    #Clase para metadatos
    class Meta:
        managed = False
        db_table = 'detalle_venta'
        verbose_name = 'Detalle de Venta'
        verbose_name_plural = 'Detalles de Venta'

#------------------------------------Clase para tabla empleado-----------------------------------------------
class Empleado(models.Model):
	#Atributos de tabla
    cod_empleado = models.IntegerField(primary_key=True)
    dpi = models.CharField(max_length=15)
    puesto = models.CharField(max_length=20)
    sueldo = models.FloatField()
    persona = models.ForeignKey('Persona', models.DO_NOTHING)

    #Clase para metadatos
    class Meta:
        managed = False
        db_table = 'empleado'
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'

#------------------------------------Clase para tabla marca-----------------------------------------------
class Marca(models.Model):
	#Atributos de tabla
    id_marca = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=25)

    #Clase para metadatos
    class Meta:
        managed = False
        db_table = 'marca'
        verbose_name = 'Marca'
        verbose_name_plural = 'Marcas'

#------------------------------------Clase para tabla pago_compra-----------------------------------------
class PagoCompra(models.Model):
	#Atributos de tabla
    id_pago_compra = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=25)
    fecha_pago = models.DateField()
    compra_num = models.ForeignKey(Compra, models.DO_NOTHING, db_column='compra_num')
    sub_total = models.FloatField()

    #Clase para metadatos
    class Meta:
        managed = False
        db_table = 'pago_compra'
        verbose_name = 'Pago de Compra'
        verbose_name_plural = 'Pagos de Compra'

#------------------------------------Clase para tabla persona---------------------------------------------
class Persona(models.Model):
	#Atributos de tabla
    id_persona = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    direccion = models.CharField(max_length=75, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    edad = models.IntegerField(blank=True, null=True)

    #Clase para metadatos
    class Meta:
        managed = False
        db_table = 'persona'
        verbose_name = 'Persona'
        verbose_name_plural = 'Personas'

#------------------------------------Clase para tabla producto--------------------------------------------
class Producto(models.Model):
	#Atributos de tabla
    cod_producto = models.CharField(primary_key=True, max_length=25)
    nombre = models.CharField(max_length=75)
    descripcion = models.CharField(max_length=100, blank=True, null=True)
    fecha_expiracion = models.DateField()
    existencia = models.IntegerField()
    marca = models.ForeignKey(Marca, models.DO_NOTHING)
    categoria = models.ForeignKey(Categoria, models.DO_NOTHING)
    precio_venta = models.FloatField()
    precio_costo = models.FloatField()

    #Clase para metadatos
    class Meta:
        managed = False
        db_table = 'producto'
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

#------------------------------------Clase para tabla proveedor-------------------------------------------
class Proveedor(models.Model):
	#Atributos de tabla
    id_proveedor = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=75)
    telefono = models.CharField(max_length=20)
    email = models.CharField(max_length=50, blank=True, null=True)

    #Clase para metadatos
    class Meta:
        managed = False
        db_table = 'proveedor'
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'

#------------------------------------Clase para tabla sucursal---------------------------------------------
class Sucursal(models.Model):
	#Atributos de tabla
    id_sucursal = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=75)
    telefono = models.CharField(max_length=20)
    email = models.CharField(max_length=50, blank=True, null=True)

    #Clase para metadatos
    class Meta:
        managed = False
        db_table = 'sucursal'
        verbose_name = 'Sucursal'
        verbose_name_plural = 'Sucursales'

#------------------------------------Clase para tabla venta-------------------------------------------------
class Venta(models.Model):
	#Atributos de tabla
    num_venta = models.AutoField(primary_key=True)
    fecha_venta = models.DateField()
    total = models.FloatField()
    cliente_nit = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='cliente_nit')
    empleado_cod = models.ForeignKey(Empleado, models.DO_NOTHING, db_column='empleado_cod')
    sucursal = models.ForeignKey(Sucursal, models.DO_NOTHING)
    auth = models.ForeignKey(AuthVenta, models.DO_NOTHING)

    #Clase para metadatos
    class Meta:
        managed = False
        db_table = 'venta'
        verbose_name = 'Venta'
        verbose_name_plural = 'Ventas'
