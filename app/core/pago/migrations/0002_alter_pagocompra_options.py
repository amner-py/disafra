# Generated by Django 3.2.5 on 2021-10-16 10:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pago', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pagocompra',
            options={'managed': False, 'verbose_name': 'Pago de Compra', 'verbose_name_plural': 'Pagos de Compras'},
        ),
    ]
