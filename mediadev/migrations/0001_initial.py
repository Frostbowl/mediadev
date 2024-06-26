# Generated by Django 5.0.6 on 2024-06-13 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('artiste', models.CharField(max_length=150)),
                ('disponible', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Dvd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('realisateur', models.CharField(max_length=150)),
                ('disponible', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='JeuDePlateau',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('createur', models.CharField(default='Unknown', max_length=150)),
                ('disponible', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Livre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('auteur', models.CharField(max_length=150)),
                ('disponible', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Membre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lastname', models.CharField(max_length=150)),
                ('firstname', models.CharField(max_length=150)),
                ('bloque', models.BooleanField(default=True)),
            ],
        ),
    ]
