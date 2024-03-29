# Generated by Django 4.1.4 on 2023-01-19 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0037_creditsale'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creditsale',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=9, verbose_name=' Monto a entregar'),
        ),
        migrations.AlterField(
            model_name='sale',
            name='estado',
            field=models.IntegerField(default=0),
        ),
    ]
