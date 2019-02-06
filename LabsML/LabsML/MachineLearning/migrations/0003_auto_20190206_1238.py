# Generated by Django 2.1.5 on 2019-02-06 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MachineLearning', '0002_tb_ml_filmes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tb_ml_filmes',
            name='distribuidora',
            field=models.CharField(blank=True, default=None, max_length=200, verbose_name='Distribuidora'),
        ),
        migrations.AlterField(
            model_name='tb_ml_filmes',
            name='genero',
            field=models.CharField(blank=True, default=None, max_length=30, verbose_name='Gêneto'),
        ),
        migrations.AlterField(
            model_name='tb_ml_filmes',
            name='nacionalidade_obra',
            field=models.CharField(blank=True, default=None, max_length=50, verbose_name='Nacionalidade'),
        ),
        migrations.AlterField(
            model_name='tb_ml_filmes',
            name='pais_produtor_obra',
            field=models.CharField(blank=True, default=None, max_length=50, verbose_name='País Produtor da Obra'),
        ),
        migrations.AlterField(
            model_name='tb_ml_filmes',
            name='titulo_obra',
            field=models.CharField(blank=True, default=None, max_length=200, verbose_name='Título'),
        ),
    ]
