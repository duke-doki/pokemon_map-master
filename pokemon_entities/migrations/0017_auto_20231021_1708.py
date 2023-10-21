# Generated by Django 3.1.14 on 2023-10-21 17:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0016_auto_20231021_1701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='previous_evolution',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='next_evolutions', to='pokemon_entities.pokemon', verbose_name='Эволюции'),
        ),
    ]