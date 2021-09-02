from django.db import models


class TipoTelefono(models.Model):
    id_tipo_telefono = models.IntegerField(db_column='ID_TIPO_TELEFONO', primary_key=True)
    tipo = models.CharField(db_column='TIPO', max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipo_telefono'


class Telefono(models.Model):
    num_telefono = models.CharField(db_column='NUM_TELEFONO', primary_key=True, max_length=16)
    tipo_telefono = models.ForeignKey(TipoTelefono, db_column='TIPO_TELEFONO_ID')
    extension = models.CharField(db_column='EXTENSION', max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'telefono'