# Generated by Django 5.0.3 on 2024-03-18 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CineEnCasa', '0005_remove_saga_elem_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='duration',
            field=models.DurationField(),
        ),
    ]