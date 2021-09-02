# Generated by Django 3.2.5 on 2021-09-02 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id_proveedor', models.IntegerField(db_column='ID_PROVEEDOR', primary_key=True, serialize=False)),
                ('nombre', models.CharField(db_column='NOMBRE', max_length=35)),
                ('correo', models.CharField(db_column='CORREO', max_length=100)),
            ],
            options={
                'db_table': 'proveedor',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Visitador',
            fields=[
                ('id_visitador', models.IntegerField(db_column='ID_VISITADOR', primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'visitador',
                'managed': False,
            },
        ),
    ]
