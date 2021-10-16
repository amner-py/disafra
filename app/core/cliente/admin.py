from django.contrib import admin
from core.cliente.models import Cliente


class ClienteAdmin(admin.ModelAdmin):
    list_display = ['nit_cliente','persona','mayorista','correo']
    list_filter = ['mayorista','correo']
    list_editable = ['correo','mayorista']
    list_per_page = 10
    search_fields = ['nit_cliente','mayorista','correo']


admin.site.register(Cliente,ClienteAdmin)
