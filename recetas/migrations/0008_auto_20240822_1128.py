# Generated by Django 3.2.25 on 2024-08-22 14:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recetas', '0007_auto_20240822_1124'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='receta',
            name='cantidad_unidades',
        ),
        migrations.RemoveField(
            model_name='receta',
            name='dosis',
        ),
        migrations.RemoveField(
            model_name='receta',
            name='medicacion',
        ),
        migrations.CreateModel(
            name='RecetaMedicacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dosis', models.CharField(max_length=200)),
                ('cantidad_unidades', models.IntegerField(default=0)),
                ('medicacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recetas.medicacion')),
                ('receta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receta_medicaciones', to='recetas.receta')),
            ],
        ),
    ]
