# Generated by Django 3.1.6 on 2021-02-15 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mukja', '0005_restaurant_head_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='golmok',
            name='head_image',
            field=models.ImageField(blank=True, upload_to='blog/%Y/%m/%d/'),
        ),
    ]
