# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-19 08:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('almacen', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='App',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hoy', models.BooleanField()),
                ('dia', models.IntegerField()),
                ('hora', models.IntegerField()),
            ],
        ),
    ]
