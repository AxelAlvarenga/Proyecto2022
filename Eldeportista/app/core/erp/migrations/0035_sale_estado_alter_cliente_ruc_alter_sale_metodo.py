# Generated by Django 4.1.4 on 2023-01-10 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0034_sale_metodo'),
    ]

    operations = [
        migrations.AddField(
            model_name='sale',
            name='estado',
            field=models.CharField(default=1, max_length=2),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cliente',
            name='Ruc',
            field=models.CharField(max_length=150, verbose_name='Ruc o CI '),
        ),
        migrations.AlterField(
            model_name='sale',
            name='metodo',
            field=models.CharField(choices=[('Credito', 'Credito'), ('Contado', 'Contado')], default='counted', max_length=10, verbose_name='Metodo de pago'),
        ),
    ]
