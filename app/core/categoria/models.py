from django.db import models


class Categoria(models.Model):
    id_categoria = models.IntegerField(db_column='ID_CATEGORIA', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='NOMBRE', max_length=35)  # Field name made lowercase.
    descripcion = models.CharField(db_column='DESCRIPCION', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'categoria'
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'


class SubCategoria(models.Model):
    id_sub_categoria = models.IntegerField(db_column='ID_SUB_CATEGORIA', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='NOMBRE', max_length=35)  # Field name made lowercase.
    categoria = models.ForeignKey(Categoria, models.DO_NOTHING, db_column='CATEGORIA_ID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sub_categoria'
        verbose_name = 'Sub-Categoria'
        verbose_name_plural = 'Sub-Categorias'