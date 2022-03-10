# Generated by Django 4.0 on 2022-03-07 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0018_alter_carimage_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='acceleration',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='tezlanish'),
        ),
        migrations.AlterField(
            model_name='car',
            name='height',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='car',
            name='length',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='car',
            name='max_speed',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='car',
            name='number_door',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='car',
            name='number_place',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='car',
            name='power_battery',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='car',
            name='power_reserve',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='quvvat_zahirasi'),
        ),
        migrations.AlterField(
            model_name='car',
            name='width',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='car',
            name='year',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
