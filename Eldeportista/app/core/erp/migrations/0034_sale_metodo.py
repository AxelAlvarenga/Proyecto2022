# Generated by Django 4.1.4 on 2023-01-10 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0033_buy_comprobante'),
    ]

    operations = [
        migrations.AddField(
            model_name='sale',
            name='metodo',
            field=models.CharField(choices=[('credit', 'Credito'), ('counted', 'Contado')], default='counted', max_length=10, verbose_name='Metodo de pago'),
        ),
    ]
