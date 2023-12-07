# Generated by Django 4.2.7 on 2023-12-06 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_rename_games_game'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='banner',
            field=models.ImageField(blank=True, null=True, upload_to='imagenes/', verbose_name='Portada'),
        ),
        migrations.AlterField(
            model_name='game',
            name='developer',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Desarollador'),
        ),
    ]