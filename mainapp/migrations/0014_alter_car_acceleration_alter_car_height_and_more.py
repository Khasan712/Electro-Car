# Generated by Django 4.0 on 2022-03-07 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0013_alter_car_max_speed_alter_car_number_door_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='acceleration',
            field=models.FloatField(blank=True, null=True, verbose_name='tezlanish'),
        ),
        migrations.AlterField(
            model_name='car',
            name='height',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='car',
            name='length',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='car',
            name='width',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
