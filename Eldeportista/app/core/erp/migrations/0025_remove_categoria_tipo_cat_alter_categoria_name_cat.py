# Generated by Django 4.1.4 on 2022-12-16 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0024_alter_categoria_name_cat_alter_categoria_tipo_cat_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categoria',
            name='tipo_cat',
        ),
        migrations.AlterField(
            model_name='categoria',
            name='name_cat',
            field=models.CharField(max_length=150, unique=True, verbose_name='Genero'),
        ),
    ]