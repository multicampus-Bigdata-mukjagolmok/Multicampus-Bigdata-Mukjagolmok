# Generated by Django 3.1.5 on 2021-02-11 09:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mukja', '0002_restaurant_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='restaurant',
            old_name='image',
            new_name='images',
        ),
    ]
