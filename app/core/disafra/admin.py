from django.contrib import admin
from .models import *

# Register your models here.
#-----------------------------------------------------------------------#
#------------------------------INLINES----------------------------------#
#-----------------------------------------------------------------------#

#------------------------------DESCUENTO--------------------------------
class DescuentoInline(admin.TabularInline):
	model=Descuento
	extra=0
#------------------------------CLIENTE----------------------------------
class ClienteInline(admin.TabularInline):
	model=Cliente
	extra=0
#------------------------------Empleado----------------------------------
class EmpleadoInline(admin.TabularInline):
	model=Empleado
	extra=0
#-------------------------CONTACTO-PROVEEDOR----------------------------
class ContactoProveedorInline(admin.TabularInline):
	model=ContactoProveedor
	extra=0
#-------------------------------VENTA-----------------------------------
class VentaInline(admin.TabularInline):
	model=Venta
	exta=0
#-----------------------------PRODUCTO----------------------------------
class ProductoInline(admin.TabularInline):
	model=Producto
	extra=0
#---------------------------DETALLE-VENTA-------------------------------
class DetalleVentaInline(admin.TabularInline):
	model=DetalleVenta
	extra=0
#---------------------------DETALLE-PRODUCTO----------------------------
class DetalleProductoInline(admin.TabularInline):
	model=DetalleProducto
	extra=0
#-------------------------------COMPRA----------------------------------
class CompraInline(admin.TabularInline):
	model=Compra
	extra=0
#-----------------------------PAGO-COMPRA-------------------------------
class PagoCompraInline(admin.TabularInline):
	model=PagoCompra
	extra=0
#---------------------------DETALLE-COMPRA------------------------------
class DetalleCompraInline(admin.TabularInline):
	model=DetalleCompra
	extra=0
#-----------------------------------------------------------------------#
#------------------------------ADMINS-----------------------------------#
#-----------------------------------------------------------------------#

#------------------------------PERSONA----------------------------------
class PersonaAdmin(admin.ModelAdmin):
	#inlines=[ClienteInline,EmpleadoInline,ContactoProveedorInline]
	search_field=['nit_cliente','nombre', 'apellido']
	list_filter=['nombre', 'apellido']
	list_display=['nombre', 'apellido']
#------------------------------PERSONA----------------------------------
class SucursalAdmin(admin.ModelAdmin):
	#inlines=[VentaInline]
	search_field=['id_sucursal','nombre']
	list_filter=['nombre']
	list_display=['nombre']

#------------------------------PERSONA----------------------------------
class AuthVentaAdmin(admin.ModelAdmin):
	#inlines=[VentaInline]
	search_field=['id_auth_venta','serie']
	list_filter=['serie']
	list_display=['serie']

#------------------------------PERSONA----------------------------------
class CategoriaAdmin(admin.ModelAdmin):
	#inlines=[ProductoInline]
	search_field=['id_categoria','nombre']
	list_filter=['nombre']
	list_display=['nombre']

#------------------------------PERSONA----------------------------------
class MarcaAdmin(admin.ModelAdmin):
	#inlines=[ProductoInline]
	search_field=['id_marca','nombre']
	list_filter=['nombre']
	list_display=['nombre']

#------------------------------PERSONA----------------------------------
class DescuentoAdmin(admin.ModelAdmin):
	#inlines=[DetalleVentaInline]
	search_field=['cod_descuento','porcentaje']
	list_filter=['porcentaje']
	list_display=['descripcion']

#------------------------------PERSONA----------------------------------
class ProveedorAdmin(admin.ModelAdmin):
	#inlines=[DetalleProductoInline,ContactoProveedorInline]
	search_field=['id_proveedor','nombre','email']
	list_filter=['nombre']
	list_display=['nombre']

#------------------------------CLIENTE----------------------------------
class ClienteAdmin(admin.ModelAdmin):
	#inlines=[VentaInline]
	search_field=['nit_cliente']
	list_filter=['nit_cliente']
	list_display=['nit_cliente']

#------------------------------Empleado----------------------------------
class EmpleadoAdmin(admin.ModelAdmin):
	#inlines=[VentaInline]
	search_field=['cod_empleado','dpi_empleado','puesto']
	list_filter=['cod_empleado']
	list_display=['cod_empleado']

#-------------------------CONTACTO-PROVEEDOR----------------------------
class ContactoProveedorAdmin(admin.ModelAdmin):
	#inlines=[CompraInline]
	search_field=['id_contacto_proveedor','proveedor']
	list_filter=['id_contacto_proveedor']
	list_display=['id_contacto_proveedor']

#-------------------------------VENTA-----------------------------------
class VentaAdmin(admin.ModelAdmin):
	inlines=[DetalleVentaInline]
	search_field=['num_venta','cliente_nit','empleado_cod','sucursal']
	list_filter=['num_venta','cliente_nit','sucursal','total']
	list_display=['num_venta','cliente_nit','sucursal','total']

#-----------------------------PRODUCTO----------------------------------
class ProductoAdmin(admin.ModelAdmin):
	#inlines=[DetalleVentaInline,DetalleProductoInline]
	search_field=['cod_producto','nombre','fecha_expiracion']
	list_filter=['cod_producto','nombre','fecha_expiracion']
	list_display=['nombre','fecha_expiracion']

#---------------------------DETALLE-VENTA-------------------------------
class DetalleProductoAdmin(admin.ModelAdmin):
	#inlines=[DetalleCompraInline]
	search_field=['id_detalle_producto','producto','proveedor']
	list_filter=['id_detalle_producto','producto','proveedor']
	list_display=['id_detalle_producto']

#---------------------------DETALLE-PROVEEDOR---------------------------
class DetalleVentaAdmin(admin.ModelAdmin):
	#inlines=[]
	search_field=['id_detalle_venta','venta_num','sub_total']
	list_filter=['id_detalle_venta','venta_num','sub_total']
	list_display=['venta_num','id_detalle_venta']

#-------------------------------COMPRA----------------------------------
class CompraAdmin(admin.ModelAdmin):
	inlines=[PagoCompraInline,DetalleCompraInline]
	search_field=['num_compra','pagado','empleado_cod','fecha_entrega']
	list_filter=['num_compra','pagado','empleado_cod','fecha_entrega']
	list_display=['num_compra','descripcion']

#-----------------------------PAGO-COMPRA-------------------------------
class PagoCompraAdmin(admin.ModelAdmin):
	#inlines=[]
	search_field=['id_pago_compra','compra_num','fecha_pago','sub_total']
	list_filter=['id_pago_compra','compra_num','fecha_pago']
	list_display=['id_pago_compra','descripcion']

#---------------------------DETALLE-COMPRA------------------------------
class DetalleCompraAdmin(admin.ModelAdmin):
	#inlines=[]
	search_field=['id_detalle_compra','compra_num','detalle_producto_id']
	list_filter=['id_detalle_compra','compra_num','detalle_producto_id']
	list_display=['id_detalle_compra','compra_num']

#-------------------------REGISTROS-DE-TABLAS---------------------------#
admin.site.register(Persona,PersonaAdmin)
admin.site.register(Sucursal,SucursalAdmin)
admin.site.register(AuthVenta,AuthVentaAdmin)
admin.site.register(Categoria,CategoriaAdmin)
admin.site.register(Marca,MarcaAdmin)
admin.site.register(Descuento,DescuentoAdmin)
admin.site.register(Proveedor,ProveedorAdmin)
admin.site.register(Cliente,ClienteAdmin)
admin.site.register(Empleado,EmpleadoAdmin)
admin.site.register(ContactoProveedor,ContactoProveedorAdmin)
admin.site.register(Venta,VentaAdmin)
admin.site.register(Producto,ProductoAdmin)
admin.site.register(DetalleVenta,DetalleVentaAdmin)
admin.site.register(DetalleProducto,DetalleProductoAdmin)
admin.site.register(Compra,CompraAdmin)
admin.site.register(PagoCompra,PagoCompraAdmin)
admin.site.register(DetalleCompra,DetalleCompraAdmin)