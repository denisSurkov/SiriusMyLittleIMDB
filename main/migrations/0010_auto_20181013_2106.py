# Generated by Django 2.1.2 on 2018-10-13 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20181012_2143'),
    ]

    operations = [
        migrations.CreateModel(
            name='FilmGenre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
            ],
            options={
                'verbose_name': 'genre',
                'verbose_name_plural': 'genres',
            },
        ),
        migrations.CreateModel(
            name='ProductionCountry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=512)),
            ],
            options={
                'verbose_name': 'production country',
                'verbose_name_plural': 'production countries',
            },
        ),
        migrations.RemoveField(
            model_name='filmmodel',
            name='genres',
        ),
        migrations.RemoveField(
            model_name='filmmodel',
            name='production_countries',
        ),
        migrations.AddField(
            model_name='filmmodel',
            name='genres',
            field=models.ManyToManyField(related_name='genres', to='main.FilmGenre'),
        ),
        migrations.AddField(
            model_name='filmmodel',
            name='production_countries',
            field=models.ManyToManyField(related_name='production_countries', to='main.ProductionCountry'),
        ),
    ]
