# Generated by Django 4.0.3 on 2022-06-13 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compdss', '0010_remove_calculation_water_density_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='calculation',
            name='port_consumption',
            field=models.CharField(default=0.0, max_length=100),
        ),
    ]
