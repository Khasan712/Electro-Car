# Generated by Django 4.0 on 2022-03-07 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0015_alter_carimage_car_alter_carimage_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='images',
            field=models.FileField(blank=True, null=True, upload_to='car/images'),
        ),
    ]
