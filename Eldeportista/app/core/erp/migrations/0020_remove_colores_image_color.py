# Generated by Django 4.1.4 on 2022-12-14 23:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0019_remove_producto_color'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='colores',
            name='image_color',
        ),
    ]
