# Generated by Django 4.0 on 2022-02-10 11:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_brend_color_car'),
    ]

    operations = [
        migrations.AddField(
            model_name='postimage',
            name='car',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='car_images', to='mainapp.car'),
        ),
    ]
