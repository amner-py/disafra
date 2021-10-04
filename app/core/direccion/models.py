from django.db import models
from core.persona.models import Persona


class Departamento(models.Model):
    id_departamento = models.IntegerField(db_column='ID_DEPARTAMENTO', primary_key=True)  # Field name made lowercase.
    departamento = models.CharField(db_column='DEPARTAMENTO', max_length=25, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'departamento'
        verbose_name = 'Departamento'
        verbose_name_plural = 'Departamentos'


class Municipio(models.Model):
    id_municipio = models.IntegerField(db_column='ID_MUNICIPIO', primary_key=True)  # Field name made lowercase.
    municipio = models.CharField(db_column='MUNICIPIO', max_length=35)  # Field name made lowercase.
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE, db_column='DEPARTAMENTO_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'municipio'
        verbose_name = 'Municipio'
        verbose_name_plural = 'Municipios'


class Direccion(models.Model):
    id_direccion = models.IntegerField(db_column='ID_DIRECCION', primary_key=True)  # Field name made lowercase.
    direccion = models.CharField(db_column='DIRECCION', max_length=150)  # Field name made lowercase.
    referencia = models.CharField(db_column='REFERENCIA', max_length=150, blank=True, null=True)  # Field name made lowercase.
    municipio = models.ForeignKey(Municipio, on_delete=models.CASCADE, db_column='MUNICIPIO_ID')  # Field name made lowercase.
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE, db_column='PERSONA_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'direccion'
        verbose_name = 'Dirección'
        verbose_name_plural = 'Direcciones'