# Generated by Django 4.0.5 on 2022-06-14 00:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0003_remove_producto_mascota_categoria_mascota_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='mascota',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mascota', to='productos.mascota'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='categoria',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='categoria', to='productos.categoria'),
        ),
    ]
