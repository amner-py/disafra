from django.contrib import admin
from core.categoria.models import Categoria,SubCategoria


class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['id_categoria','nombre','descripcion']
    list_filter = ['nombre']
    list_editable = ['descripcion']
    list_per_page = 10
    search_fields = ['nombre']


class SubCategoriaAdmin(admin.ModelAdmin):
    list_display = ['id_sub_categoria','nombre','categoria','producto_cod']
    list_filter = ['nombre','categoria','producto_cod']
    list_editable = ['categoria','producto_cod']
    list_per_page = 10
    search_fields = ['nombre','categoria','producto_cod']


admin.site.register(Categoria,CategoriaAdmin)
admin.site.register(SubCategoria,SubCategoriaAdmin)
