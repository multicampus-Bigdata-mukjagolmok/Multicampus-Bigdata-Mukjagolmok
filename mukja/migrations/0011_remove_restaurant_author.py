# Generated by Django 3.1.5 on 2021-02-16 14:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mukja', '0010_auto_20210216_2345'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurant',
            name='author',
        ),
    ]