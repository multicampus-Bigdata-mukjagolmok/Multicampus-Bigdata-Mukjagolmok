# Generated by Django 3.1.6 on 2021-02-15 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mukja', '0004_auto_20210215_1147'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='head_image',
            field=models.ImageField(blank=True, upload_to='blog/%Y/%m/%d/'),
        ),
    ]