# Generated by Django 3.2.5 on 2021-09-02 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Permiso',
            fields=[
                ('permiso', models.CharField(db_column='PERMISO', max_length=30, primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'permiso',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PermisoUsuarioSucursal',
            fields=[
                ('id_permiso_usuario_sucursal', models.IntegerField(db_column='ID_PERMISO_USUARIO_SUCURSAL', primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'permiso_usuario_sucursal',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Sucursal',
            fields=[
                ('id_sucursal', models.IntegerField(db_column='ID_SUCURSAL', primary_key=True, serialize=False)),
                ('nombre', models.CharField(db_column='NOMBRE', max_length=35)),
                ('correo', models.CharField(db_column='CORREO', max_length=100)),
            ],
            options={
                'db_table': 'sucursal',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UsuarioSucursal',
            fields=[
                ('usuario_sucursal', models.CharField(db_column='USUARIO_SUCURSAL', max_length=50, primary_key=True, serialize=False)),
                ('pass_field', models.CharField(db_column='PASS', max_length=64)),
                ('activo', models.CharField(db_column='ACTIVO', max_length=1)),
                ('fecha_creado', models.DateField(blank=True, db_column='FECHA_CREADO', null=True)),
            ],
            options={
                'db_table': 'usuario_sucursal',
                'managed': False,
            },
        ),
    ]