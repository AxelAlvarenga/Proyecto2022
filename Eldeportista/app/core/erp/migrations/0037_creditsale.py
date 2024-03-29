# Generated by Django 4.1.4 on 2023-01-18 23:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0036_alter_sale_metodo'),
    ]

    operations = [
        migrations.CreateModel(
            name='CreditSale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=9, verbose_name='Monto a entregar')),
                ('sale', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='erp.sale')),
            ],
            options={
                'verbose_name': '',
                'verbose_name_plural': '',
                'ordering': ['id'],
            },
        ),
    ]
