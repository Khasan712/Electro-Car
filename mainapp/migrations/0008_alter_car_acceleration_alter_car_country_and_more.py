# Generated by Django 4.0 on 2022-03-07 13:25

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0007_alter_car_brend'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='acceleration',
            field=models.FloatField(blank=True, verbose_name='tezlanish'),
        ),
        migrations.AlterField(
            model_name='car',
            name='country',
            field=django_countries.fields.CountryField(blank=True, max_length=2),
        ),
        migrations.AlterField(
            model_name='car',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='car',
            name='height',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='car',
            name='length',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='car',
            name='max_speed',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='car',
            name='number_door',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='car',
            name='number_place',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='car',
            name='power_battery',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='car',
            name='power_motor',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='car',
            name='power_reserve',
            field=models.IntegerField(blank=True, verbose_name='quvvat_zahirasi'),
        ),
        migrations.AlterField(
            model_name='car',
            name='type_body',
            field=models.CharField(blank=True, max_length=300, verbose_name='kuzov'),
        ),
        migrations.AlterField(
            model_name='car',
            name='width',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='car',
            name='year',
            field=models.IntegerField(blank=True),
        ),
    ]