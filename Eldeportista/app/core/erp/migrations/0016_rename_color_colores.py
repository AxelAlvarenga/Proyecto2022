# Generated by Django 4.1.4 on 2022-12-14 18:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0015_producto_cantidad_alter_producto_image'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='color',
            new_name='colores',
        ),
    ]
