# Generated by Django 4.0 on 2022-02-08 14:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Image',
            new_name='PostImage',
        ),
    ]