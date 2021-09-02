# Generated by Django 3.2.5 on 2021-09-02 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Telefono',
            fields=[
                ('num_telefono', models.CharField(db_column='NUM_TELEFONO', max_length=16, primary_key=True, serialize=False)),
                ('extension', models.CharField(blank=True, db_column='EXTENSION', max_length=5, null=True)),
            ],
            options={
                'db_table': 'telefono',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TipoTelefono',
            fields=[
                ('id_tipo_telefono', models.IntegerField(db_column='ID_TIPO_TELEFONO', primary_key=True, serialize=False)),
                ('tipo', models.CharField(blank=True, db_column='TIPO', max_length=15, null=True)),
            ],
            options={
                'db_table': 'tipo_telefono',
                'managed': False,
            },
        ),
    ]