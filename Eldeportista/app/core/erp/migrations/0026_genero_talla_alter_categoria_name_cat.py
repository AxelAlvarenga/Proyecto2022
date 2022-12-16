# Generated by Django 4.1.4 on 2022-12-16 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0025_remove_categoria_tipo_cat_alter_categoria_name_cat'),
    ]

    operations = [
        migrations.CreateModel(
            name='genero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genero', models.CharField(max_length=150, unique=True, verbose_name='Genero')),
            ],
            options={
                'verbose_name': 'Genero',
                'verbose_name_plural': 'Generos',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Talla',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Talla', models.CharField(max_length=150, unique=True, verbose_name='Talla')),
            ],
            options={
                'verbose_name': 'Talla',
                'verbose_name_plural': 'Tallas',
                'ordering': ['id'],
            },
        ),
        migrations.AlterField(
            model_name='categoria',
            name='name_cat',
            field=models.CharField(max_length=150, unique=True, verbose_name='Categoria'),
        ),
    ]
