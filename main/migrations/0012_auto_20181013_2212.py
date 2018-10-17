# Generated by Django 2.1.2 on 2018-10-13 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_auto_20181013_2106'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='filmmodel',
            name='genres',
        ),
        migrations.RemoveField(
            model_name='filmmodel',
            name='production_countries',
        ),
        migrations.AddField(
            model_name='filmgenre',
            name='films',
            field=models.ManyToManyField(related_name='films', to='main.FilmModel'),
        ),
        migrations.AddField(
            model_name='productioncountry',
            name='films',
            field=models.ManyToManyField(related_name='films_country', to='main.FilmModel'),
        ),
    ]
