# Generated by Django 4.1.4 on 2023-01-10 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0035_sale_estado_alter_cliente_ruc_alter_sale_metodo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='metodo',
            field=models.CharField(choices=[('Credito', 'Credito'), ('Contado', 'Contado')], default='Contado', max_length=10, verbose_name='Metodo de pago'),
        ),
    ]
