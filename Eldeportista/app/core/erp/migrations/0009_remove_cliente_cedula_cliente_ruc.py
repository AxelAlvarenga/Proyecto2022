# Generated by Django 4.0.2 on 2022-11-09 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0008_alter_cliente_cedula'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='cedula',
        ),
        migrations.AddField(
            model_name='cliente',
            name='Ruc',
            field=models.CharField(default=1, max_length=150, verbose_name='Ruc'),
            preserve_default=False,
        ),
    ]
