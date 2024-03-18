# Generated by Django 5.0.3 on 2024-03-18 14:03

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('release_year', models.PositiveIntegerField()),
                ('duration', models.TimeField()),
                ('country', models.CharField(choices=[('US', 'United States'), ('ESP', 'Spain'), ('UK', 'United Kingdom'), ('JAP', 'Japan'), ('KO', 'Korea'), ('CAT', 'Catalonia'), ('IRE', 'Ireland')], max_length=20)),
                ('synopsis', models.TextField()),
                ('poster', models.ImageField(upload_to='')),
                ('type', models.CharField(choices=[('SAGA', 'SAGA'), ('MOVIE', 'PELÍCULA'), ('DOCU-SERIES', 'DOCU-SERIE'), ('EVENT', 'EVENTO'), ('TV_SHOW', 'SERIE'), ('TV_PROGRAM', 'PROGRAMA'), ('DOCUMENTARY', 'DOCUMENTAL')], max_length=15)),
                ('platform', models.CharField(choices=[('DISNEY_PLUS', 'Disney+'), ('NETFLIX', 'Netflix'), ('MOVISTAR_PLUS', 'Movistar+'), ('PRIME_VIDEO', 'Prime Video'), ('YOUTUBE', 'YouTube'), ('HBO_MAX', 'HBO Max'), ('FILMIN', 'Filmin')], max_length=15)),
                ('is_saga', models.BooleanField()),
                ('total_films', models.PositiveIntegerField(default='3')),
                ('current_film', models.PositiveIntegerField(default='1')),
                ('saga_type', models.CharField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='BillboardFilm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hour', models.TimeField(default='20:00')),
                ('day', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(31)])),
                ('month', models.CharField(choices=[('JAN', 'Enero'), ('FEB', 'Febrero'), ('MAR', 'Marzo'), ('APR', 'Abril'), ('MAY', 'Mayo'), ('JUN', 'Junio'), ('JUL', 'Julio'), ('AUG', 'Agosto'), ('SEP', 'Septiembre'), ('OCT', 'Octubre'), ('NOV', 'Noviembre'), ('DEC', 'Diciembre')], max_length=10)),
                ('film', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CineEnCasa.film')),
            ],
        ),
        migrations.CreateModel(
            name='Billboard',
            fields=[
                ('week', models.AutoField(primary_key=True, serialize=False)),
                ('films', models.ManyToManyField(blank=True, to='CineEnCasa.film')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.DecimalField(decimal_places=1, max_digits=3)),
                ('comment', models.TextField()),
                ('film', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CineEnCasa.film')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]