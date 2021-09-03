from django.contrib import admin
from core.cliente.models import Cliente,UsuarioCliente


class UsuarioClienteAdmin(admin.ModelAdmin):
    list_display = ['correo','pass_field','activo','fecha_creado']
    list_filter = ['activo','fecha_creado']
    list_editable = ['activo']
    list_per_page = 10
    search_fields = ['correo','activo','fecha_creado']


class ClienteAdmin(admin.ModelAdmin):
    list_display = ['nit_cliente','persona','mayorista','correo']
    list_filter = ['mayorista','correo']
    list_editable = ['correo','mayorista']
    list_per_page = 10
    search_fields = ['nit_cliente','mayorista','correo']


admin.site.register(UsuarioCliente,UsuarioClienteAdmin)
admin.site.register(Cliente,ClienteAdmin)
