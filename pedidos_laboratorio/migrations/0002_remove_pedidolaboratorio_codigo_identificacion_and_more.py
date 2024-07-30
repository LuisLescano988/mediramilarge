# Generated by Django 5.0.4 on 2024-07-30 20:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pacientes', '0004_alter_paciente_provincia'),
        ('pedidos_laboratorio', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pedidolaboratorio',
            name='codigo_identificacion',
        ),
        migrations.RemoveField(
            model_name='pedidolaboratorio',
            name='dni',
        ),
        migrations.RemoveField(
            model_name='pedidolaboratorio',
            name='nombre_apellido',
        ),
        migrations.RemoveField(
            model_name='pedidolaboratorio',
            name='numero_afiliado',
        ),
        migrations.RemoveField(
            model_name='pedidolaboratorio',
            name='obra_social',
        ),
        migrations.AddField(
            model_name='pedidolaboratorio',
            name='paciente',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='pacientes.paciente'),
            preserve_default=False,
        ),
    ]
