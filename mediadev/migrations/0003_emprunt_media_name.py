# Generated by Django 5.0.6 on 2024-06-18 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mediadev', '0002_alter_membre_bloque_emprunt'),
    ]

    operations = [
        migrations.AddField(
            model_name='emprunt',
            name='media_name',
            field=models.CharField(default='Unknow', max_length=150),
        ),
    ]
