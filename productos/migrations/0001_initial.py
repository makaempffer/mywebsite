# Generated by Django 4.0.5 on 2022-06-16 15:43

from django.db import migrations, models
import django.db.models.deletion
import pathlib


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.TextField(max_length=64)),
                ('descripcion', models.TextField(default='', max_length=512)),
                ('imagen', models.ImageField(null=True, upload_to=pathlib.PureWindowsPath('C:/Users/Cetecom/Desktop/mywebsite/media/categorias'))),
            ],
        ),
        migrations.CreateModel(
            name='Mascota',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.TextField(max_length=64)),
                ('descripcion', models.TextField(default='', max_length=512)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.TextField(max_length=64)),
                ('descripcion', models.TextField(max_length=512)),
                ('precio', models.PositiveIntegerField()),
                ('stock', models.IntegerField()),
                ('imagen', models.ImageField(null=True, upload_to=pathlib.PureWindowsPath('C:/Users/Cetecom/Desktop/mywebsite/media/productos'))),
                ('categoria', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='categoria', to='productos.categoria')),
            ],
        ),
        migrations.AddField(
            model_name='categoria',
            name='mascota',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mascota', to='productos.mascota'),
        ),
    ]