# Generated by Django 2.1.2 on 2018-10-12 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20181012_1909'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filmmodel',
            name='imdb_id',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='filmmodel',
            name='original_language',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='filmmodel',
            name='status',
            field=models.CharField(max_length=64, null=True),
        ),
    ]