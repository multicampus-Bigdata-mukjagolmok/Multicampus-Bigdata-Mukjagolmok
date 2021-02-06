# Generated by Django 3.1.6 on 2021-02-05 07:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Golmok',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, unique=True)),
                ('address', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, unique=True)),
                ('address', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=500)),
                ('rating', models.CharField(max_length=10)),
                ('golmok', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='mukja.golmok')),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, unique=True)),
                ('price', models.CharField(max_length=10, unique=True)),
                ('description', models.CharField(max_length=300, unique=True)),
                ('restaurant', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='mukja.restaurant')),
            ],
        ),
    ]
