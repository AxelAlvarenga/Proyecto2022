# Generated by Django 4.1.4 on 2022-12-12 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0012_producto_cat_alter_categoria_name_cat'),
    ]

    operations = [
        migrations.CreateModel(
            name='color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_color', models.CharField(max_length=150, unique=True, verbose_name='Nombre_color')),
                ('image_color', models.ImageField(blank=True, null=True, upload_to='product/%Y/%m/%d')),
            ],
            options={
                'verbose_name': 'color',
                'verbose_name_plural': 'colores',
                'ordering': ['id'],
            },
        ),
    ]