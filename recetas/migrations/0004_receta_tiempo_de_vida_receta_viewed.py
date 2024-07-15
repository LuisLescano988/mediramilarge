# Generated by Django 5.0.4 on 2024-07-15 19:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recetas', '0003_remove_receta_dni_remove_receta_nombre_completo_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='receta',
            name='tiempo_de_vida',
            field=models.DurationField(default=datetime.timedelta(days=7)),
        ),
        migrations.AddField(
            model_name='receta',
            name='viewed',
            field=models.BooleanField(default=False),
        ),
    ]
