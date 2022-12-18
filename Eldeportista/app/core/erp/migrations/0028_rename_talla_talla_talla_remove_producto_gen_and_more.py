# Generated by Django 4.1.4 on 2022-12-16 21:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0027_producto_gen_alter_categoria_name_cat_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='talla',
            old_name='Talla',
            new_name='talla',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='gen',
        ),
        migrations.AddField(
            model_name='producto',
            name='gender',
            field=models.CharField(choices=[('male', 'Masculino'), ('female', 'Femenino'), ('child', 'Niños')], default='male', max_length=10, verbose_name='Genero'),
        ),
        migrations.AddField(
            model_name='talla',
            name='cat',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='erp.categoria', verbose_name='Categoría'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='genero',
        ),
    ]