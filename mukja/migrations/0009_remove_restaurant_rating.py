# Generated by Django 3.1.6 on 2021-02-15 16:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mukja', '0008_auto_20210215_1546'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurant',
            name='rating',
        ),
    ]
