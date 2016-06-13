# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-06-13 18:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_categoria', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Estadistica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=30)),
                ('cantidad', models.DecimalField(decimal_places=2, max_digits=30)),
                ('mes', models.CharField(choices=[('01', 'Enero'), ('02', 'Febrero'), ('03', 'Marzo'), ('04', 'Abril'), ('05', 'Mayo'), ('06', 'Junio'), ('07', 'Julio'), ('08', 'Agosto'), ('09', 'Septiembre'), ('10', 'Octubre'), ('11', 'Noviembre'), ('12', 'Diciembre')], default='01', max_length=2)),
                ('anho', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('codigo', models.CharField(max_length=8, primary_key=True, serialize=False, unique=True)),
                ('nombre_producto', models.TextField()),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='importaciones.Categoria')),
            ],
        ),
        migrations.AddField(
            model_name='estadistica',
            name='producto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='importaciones.Producto'),
        ),
        migrations.AlterUniqueTogether(
            name='estadistica',
            unique_together=set([('producto', 'mes', 'anho')]),
        ),
    ]