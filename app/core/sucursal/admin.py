from django.contrib import admin
from core.sucursal.models import Sucursal,UsuarioSucursal,PermisoUsuarioSucursal,Permiso


class SucursalAdmin(admin.ModelAdmin):
    list_display = ['id_sucursal','nombre','correo','direccion','telefono_num']
    list_filter = []
    list_editable = ['nombre','correo','direccion','telefono_num']
    list_per_page = 10
    search_fields = ['nombre','correo','telefono_num']


class UsuarioSucursalAdmin(admin.ModelAdmin):
    list_display = ['usuario_sucursal','pass_field','activo','fecha_creado','sucursal']
    list_filter = ['activo','sucursal','fecha_creado']
    list_editable = ['pass_field','activo']
    list_per_page = 10
    search_fields = ['sucursal']


class PermisoAdmin(admin.ModelAdmin):
    list_display = ['permiso']
    list_filter = []
    list_editable = []
    list_per_page = 10
    search_fields = ['permiso']


class PermisoUsuarioSucursalAdmin(admin.ModelAdmin):
    list_display = ['id_permiso_usuario_sucursal','sucursal_usuario','permiso']
    list_filter = ['permiso']
    list_editable = ['sucursal_usuario','permiso']
    list_per_page = 10
    search_fields = ['sucursal_usuario','permiso']


admin.site.register(Sucursal,SucursalAdmin)
admin.site.register(UsuarioSucursal,UsuarioSucursalAdmin)
admin.site.register(Permiso,PermisoAdmin)
admin.site.register(PermisoUsuarioSucursal,PermisoUsuarioSucursalAdmin)