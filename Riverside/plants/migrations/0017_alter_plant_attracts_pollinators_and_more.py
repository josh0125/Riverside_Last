# Generated by Django 4.1.2 on 2023-05-25 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plants', '0016_plant_this_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plant',
            name='attracts_pollinators',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
        migrations.AlterField(
            model_name='plant',
            name='deer_resistant',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
        migrations.AlterField(
            model_name='plant',
            name='drought_tolerant',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
        migrations.AlterField(
            model_name='plant',
            name='ground_cover',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
    ]
