# Generated by Django 4.0 on 2022-03-07 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0017_alter_car_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carimage',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='image'),
        ),
    ]
